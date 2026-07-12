# 010 — Performance/QA rig built; local-model limits probed

**Date:** 2026-07-12. Extends the rig concept from notebook 009 into a
working end-to-end system, then uses it to characterize the local model.

## The rig (all on homelab infrastructure)

Full chain, verified working:

**Fieldy pendant → cloud → webhook → alien archive → herman (brain) →
oracle (local LLM) → alien (feed file) → MatrixPortal panel.**

- **Display node** ([`../src/heckler_panel/`](../src/heckler_panel/)):
  Adafruit MatrixPortal M4 + P6 64×32 HUB75 panel. Joined lab Wi-Fi
  (SSID typo diagnosed via the ESP32's own network scan), polls a feed
  file on alien's signage server. Evolved single-line → dual-line →
  single fast small-font mixed-case. Bright enough for outdoor use;
  stable on a Mac USB-C port at moderate brightness (stage use wants a
  separate 5 V supply).
- **Brains** ([`../src/heckler_brain/`](../src/heckler_brain/)): two
  personas over the same pipeline — `heckler_brain.py` (deadpan roast)
  and `qa_brain.py` (factual answers). Both gated on a flag file so
  ambient speech is never processed. Local model: qwen2.5:14b-instruct
  on oracle.
- Latency end-to-end ≈ conversation-end + ~15 s (Fieldy processing
  dominates; local LLM ~3–5 s).

## Deliberate probe of the local model's answer boundaries

Researcher asked a designed battery of spoken questions (full Q&A in
[`../data/qa-log-2026-07-12.md`](../data/qa-log-2026-07-12.md)):

| Class | Question | Model answer | Verdict |
|---|---|---|---|
| Verifiable fact | US national parks | 63 | correct |
| Verifiable fact | Hawaii main islands | 8 | correct |
| Pop-culture trivia | Tootsie Pop "wise owl" licks | "1000" | **wrong** (ad says three) |
| Verifiable fact | orig. VW Beetle passengers | 4 | ~correct |
| Unknowable personal | a family member's location | "location unknown" | **appropriate refusal** |
| Unknowable personal | researcher's own location | "check GPS/map app" | **appropriate refusal** |
| Time-sensitive | current US President | "Joe Biden" | **stale** (see below) |

### Findings

1. **Stale knowledge stated confidently.** qwen2.5:14b's training predates
   the Nov 2024 election, so its "current President" answer reflects the
   cutoff, not July 2026 — delivered with no hedge. An offline model cannot
   answer time-sensitive questions past its cutoff; that stage would need a
   web-search tool or a refreshed model. **Core limitation for any
   assistive deployment.**
2. **Confabulation on trivia.** The Tootsie Pop miss shows the 14B model
   will invent a specific wrong number rather than say "unknown" on
   low-stakes pop-culture facts.
3. **Appropriate refusals on unknowable personal questions** — asked where a
   person was, it declined instead of inventing. The most encouraging result
   for assistive use: the failure mode on personal facts is refusal, not
   fabrication (opposite of the trivia behavior).
4. **Formatting instructions partially ignored** — sentence-case + keep-
   acronyms-capitalized only intermittently obeyed ("hawaii", "joe biden",
   "usa"). Small models follow soft style rules unreliably.

## Assessment

Pipeline: flawless. Model: bounded exactly as a small offline LLM should be.
The refusal-vs-confabulation split (refuses on people, invents on trivia) is
the notable behavioral finding and directly relevant to whether a local
model is safe as the AI layer in an assistive build.
