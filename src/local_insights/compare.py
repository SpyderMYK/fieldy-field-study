#!/usr/bin/env python3
"""Local-LLM control for Fieldy's AI layer (summaries + task extraction).

Feeds each archived conversation transcript to a local Ollama model and
prints its summary/tasks next to Fieldy's cloud-generated ones, so the
cloud AI layer can be judged against an on-prem baseline.

Stdlib only. Ollama is reached over SSH (stays localhost-bound on its
host). Fieldy transcripts/summaries come from the public API.

Usage:
  python3 compare.py [--model qwen2.5:14b-instruct] [--hours 48]

Requires:
  - Fieldy API key in ~/.config/fieldy/api_key
  - SSH alias for the Ollama host (default: oracle)
"""
import argparse
import datetime as dt
import json
import subprocess

FIELDY = "https://api.fieldy.ai/api/public/v2"

PROMPT = """You are an assistant processing a conversation transcript from a \
wearable recorder. Produce STRICT JSON with two keys:
"summary": a 2-3 sentence summary of the conversation;
"tasks": a list of objects {{"title": str, "due": str|null}} for every \
commitment or action item a speaker takes on. Empty list if none.
Transcript:
---
{transcript}
---
JSON only, no markdown fences."""


def fieldy_get(path, key):
    out = subprocess.run(
        ["curl", "-s", "-m", "30",
         "-H", "Authorization: Bearer " + key, FIELDY + path],
        capture_output=True, text=True, timeout=40)
    return json.loads(out.stdout)


def ollama(ssh_host, model, prompt):
    payload = json.dumps({
        "model": model, "prompt": prompt, "stream": False,
        "format": "json", "options": {"temperature": 0.2},
    })
    out = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", ssh_host,
         "curl -s -m 300 http://127.0.0.1:11434/api/generate "
         "-d @- -H 'Content-Type: application/json'"],
        input=payload, capture_output=True, text=True, timeout=320)
    return json.loads(json.loads(out.stdout)["response"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen2.5:14b-instruct")
    ap.add_argument("--ssh-host", default="oracle")
    ap.add_argument("--hours", type=int, default=48)
    args = ap.parse_args()

    key = open(
        __import__("os").path.expanduser("~/.config/fieldy/api_key")
    ).read().strip()

    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(hours=args.hours)
    fmt = lambda t: t.strftime("%Y-%m-%dT%H:%M:%SZ")

    convs = fieldy_get(
        f"/conversations?startTime={fmt(start)}&endTime={fmt(end)}", key
    )["items"]
    segs = fieldy_get(
        f"/transcriptions?startTime={fmt(start)}&endTime={fmt(end)}", key
    )["items"]

    for c in convs:
        if c["title"] == "No speech detected":
            continue
        mine = [s for s in segs
                if c["startTime"] <= s["timestamp"] <= c["endTime"]]
        if not mine:
            continue
        transcript = "\n".join(
            f"[{s['speaker']}] {s['text']}" for s in mine)
        local = ollama(args.ssh_host, args.model,
                       PROMPT.format(transcript=transcript))
        print("=" * 72)
        print(f"CONVERSATION: {c['title']}  ({c['startTime']})")
        print(f"\n--- Fieldy cloud summary:\n{c['summary']}")
        print(f"\n--- Local {args.model} summary:\n{local.get('summary')}")
        print(f"\n--- Local extracted tasks: "
              f"{json.dumps(local.get('tasks'), indent=1)}")


if __name__ == "__main__":
    main()
