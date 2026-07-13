#!/usr/bin/env python3
"""Heckler brain: Fieldy transcript -> local LLM roast -> LED panel feed.

Watches the Fieldy webhook archive on alien; on each new speech-bearing
conversation, asks the local model (Ollama on oracle) for a two-line
deadpan roast and writes it to the panel's feed file. Runs only while a
show-mode flag exists, so ambient conversation is never editorialized.

Topology (rehearsal): runs on herman, which can SSH to both alien
(archive + panel feed) and oracle (localhost-bound Ollama).
Stdlib only.

Usage:
  touch /tmp/HECKLER_SHOW_ON   # enable
  python3 heckler_brain.py
  rm /tmp/HECKLER_SHOW_ON      # silence
"""
import json
import os
import subprocess
import time

ALIEN = "mike@alien.lan"
ORACLE = "oracle"
ARCHIVE_GLOB = "/tank/fieldy/raw/webhooks-*.jsonl"
FEED_FILE = "/opt/signage/heckler.txt"
BUS_FILE = "/opt/signage/heckler.json"
SHOW_FLAG = os.path.expanduser("~/.heckler_show_on")
MODEL = "qwen2.5:14b-instruct"
POLL = 5

PROMPT = (
    "You are a deadpan AI comedian heckling a presenter who is wearing a "
    "recording pendant and CANNOT see the screen where your words appear. "
    "Below is a transcript of what they just said. Respond with STRICT JSON: "
    '{{"line1": str, "line2": str}} - two short punchy roast lines, each at '
    "most 40 characters, all caps, no profanity, no emoji. Roast the CONTENT "
    "of what they said. Transcript:\n---\n{transcript}\n---\nJSON only."
)


def sh(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)


def latest_conversation():
    """Return (marker, transcript) for the newest speech-bearing payload."""
    out = sh(["ssh", "-o", "BatchMode=yes", ALIEN,
              f"cat {ARCHIVE_GLOB} 2>/dev/null | tail -1"], timeout=30)
    if not out.stdout.strip():
        return None, None
    ev = json.loads(out.stdout)
    body = json.loads(ev["body"])
    text = body.get("transcription", "").strip()
    if not text:
        return None, None
    return ev["received_at"], text


def roast(transcript):
    payload = json.dumps({
        "model": MODEL, "prompt": PROMPT.format(transcript=transcript),
        "stream": False, "format": "json", "options": {"temperature": 0.8},
    })
    out = sh(["ssh", "-o", "BatchMode=yes", ORACLE,
              "curl -s -m 300 http://127.0.0.1:11434/api/generate "
              "-d @- -H 'Content-Type: application/json'"],
             input=payload, timeout=320)
    obj = json.loads(json.loads(out.stdout)["response"])
    return obj.get("line1", ""), obj.get("line2", "")


def publish(mode, line1, line2):
    """Write the plain-text projection (LED node) and the JSON bus."""
    short = (line1 + " " + line2).strip()
    bus = json.dumps({"ts": time.time(), "mode": mode, "line1": line1,
                      "line2": line2, "short": short, "full": short})
    sh(["ssh", "-o", "BatchMode=yes", ALIEN,
        f"sudo tee {FEED_FILE} >/dev/null"], input=f"{line1}\n{line2}\n",
       timeout=30)
    sh(["ssh", "-o", "BatchMode=yes", ALIEN,
        f"sudo tee {BUS_FILE} >/dev/null"], input=bus, timeout=30)


def main():
    print("heckler brain up. show flag:", SHOW_FLAG)
    seen = None
    while True:
        if os.path.exists(SHOW_FLAG):
            marker, transcript = latest_conversation()
            if marker and marker != seen:
                seen = marker
                try:
                    l1, l2 = roast(transcript)
                    print(f"ROAST: {l1} / {l2}")
                    publish("roast", l1, l2)
                except Exception as e:
                    print("roast failed:", repr(e))
        time.sleep(POLL)


if __name__ == "__main__":
    main()
