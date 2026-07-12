#!/usr/bin/env python3
"""Q&A brain: Fieldy question -> local LLM answer -> LED panel feed.

Same pipeline as heckler_brain, but the local model ANSWERS the spoken
question concisely for the panel instead of roasting. This is the
training/QA mode of the performance rig.

Runs on herman (SSH reach to alien + oracle). Stdlib only.
Gate: runs only while ~/.qa_on exists.
"""
import json
import os
import subprocess
import time

ALIEN = "mike@alien.lan"
ORACLE = "oracle"
ARCHIVE_GLOB = "/tank/fieldy/raw/webhooks-*.jsonl"
FEED_FILE = "/opt/signage/heckler.txt"
FLAG = os.path.expanduser("~/.qa_on")
MODEL = "qwen2.5:14b-instruct"
POLL = 5

PROMPT = (
    "The following is a question or topic spoken aloud by someone. Answer it "
    "for a small 2-line LED sign. Respond with STRICT JSON: "
    '{{"line1": str, "line2": str}} - a correct, concise answer split across '
    "two lines, each at most 42 characters, ALL CAPS, no emoji. If it is not "
    "a question, give the single most useful fact about the topic. "
    "Spoken input:\n---\n{q}\n---\nJSON only."
)


def sh(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)


def latest(marker_seen):
    out = sh(["ssh", "-o", "BatchMode=yes", ALIEN,
              f"cat {ARCHIVE_GLOB} 2>/dev/null | tail -1"], timeout=30)
    if not out.stdout.strip():
        return None, None
    ev = json.loads(out.stdout)
    if ev["received_at"] == marker_seen:
        return None, None
    text = json.loads(ev["body"]).get("transcription", "").strip()
    return (ev["received_at"], text) if text else (ev["received_at"], None)


def answer(q):
    payload = json.dumps({
        "model": MODEL, "prompt": PROMPT.format(q=q), "stream": False,
        "format": "json", "options": {"temperature": 0.3},
    })
    out = sh(["ssh", "-o", "BatchMode=yes", ORACLE,
              "curl -s -m 300 http://127.0.0.1:11434/api/generate "
              "-d @- -H 'Content-Type: application/json'"],
             input=payload, timeout=320)
    obj = json.loads(json.loads(out.stdout)["response"])
    return obj.get("line1", ""), obj.get("line2", "")


def push(l1, l2):
    sh(["ssh", "-o", "BatchMode=yes", ALIEN,
        f"sudo tee {FEED_FILE} >/dev/null"], input=f"{l1}\n{l2}\n", timeout=30)


def main():
    print("Q&A brain up. flag:", FLAG)
    seen = None
    while True:
        if os.path.exists(FLAG):
            marker, text = latest(seen)
            if marker:
                seen = marker
                if text:
                    try:
                        l1, l2 = answer(text)
                        print(f"Q: {text[:60]}\nA: {l1} / {l2}")
                        push(l1, l2)
                    except Exception as e:
                        print("answer failed:", repr(e))
        time.sleep(POLL)


if __name__ == "__main__":
    main()
