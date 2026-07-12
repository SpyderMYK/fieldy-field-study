# 008 — Local LLM enters the workflow; cloud AI layer gets a control

**Date:** 2026-07-12. New instrument:
[`../src/local_insights/compare.py`](../src/local_insights/compare.py).

## Setup

Ollama on the homelab's Apple Silicon host (8 models available; harness
default **qwen2.5:14b-instruct**), reached over SSH so the Ollama API stays
localhost-bound — no service exposure needed. Stdlib-only Python on the
study workstation pulls transcripts + summaries from the Fieldy API, asks
the local model for a summary and task extraction per conversation, and
prints side-by-sides.

## First run (5 conversations)

**Summaries:** Fieldy's cloud summaries are more polished and detailed;
the local 14B is competent but occasionally clunkier and once inferred
beyond the data ("9:27 **AM**" — meridiem never spoken). No factual
inventions by either side beyond that.

**Task extraction — the finding:**

- **Fieldy: 0 tasks extracted across all conversations to date**
  (`/tasks` empty at every status), including Script C's explicit dated
  imperative ("Email the CSV to procurement by Friday the twenty-first…").
- **Local qwen2.5:14b: caught it** ("Email CSV to procurement by Friday,
  21st"), first pass, temperature 0.2.
- Caveat: Fieldy's extraction may be gated (templates, conversation types,
  app-side review flow) — script D's six-commitment dialogue remains the
  designed test. But as observed so far, the local model leads on the
  vendor's marquee feature.

**TV contamination reaches the summary layer [key finding]:** Fieldy's
summary of the TV take (entry 004) opens "**You discussed** a professional
investigation…" — broadcast fiction attributed to the wearer, in second
person, in the AI narrative of the day. The phantom-conversation problem
propagates from transcript to insights.

**Housekeeping:** the previously unattributed 17:29 conversation
self-identifies in its summary as the researcher's LED check (entry 006
observation, now attributed).

## Assessment

The homelab control is now standing: STT layer (whisper.cpp, planned) and
AI layer (Ollama, running) both have local baselines. For the assistive
architecture, the local model handling extraction competently is an
existence proof that the privacy-preserving path (webhook → local archive
→ local LLM) can replace the cloud AI layer.
