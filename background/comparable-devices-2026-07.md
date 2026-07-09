# Comparable devices and recording methods — landscape check, 2026-07-08

Quick verified sweep before Day 1, updating the pre-arrival report's section
on adjacent ecosystems. **Source-quality caveat:** much of the public
comparison content is vendor-authored (Plaud's and UMEVO's blogs review their
own categories), so competitive claims below are tagged to their sources and
treated as marketing until independently confirmed.

## The wearable field as of mid-2026

| Device | Status | Notes |
|---|---|---|
| **Limitless Pendant** | **Acquired by Meta, Dec 2025; hardware no longer sold** | The ecosystem our background report drew MCP/API patterns from is now frozen. The open-source integration patterns (mcp-limitless and forks) remain valid as *code references*, but Limitless is no longer a viable comparison device to buy. |
| **Bee** | Owned by **Amazon** | Always-on pendant, summaries/reminders/insights. Cloud-tied; acquisition raises the same data-path questions we flagged for Fieldy. |
| **Omi** | Independent, **fully open-source (hardware + software)**, ~$89 | The most interesting comparison device for this study: open firmware/backend means its pipeline is inspectable in ways Fieldy's is not, and reviewers report HIPAA/SOC 2 posture unusual for an open project. Candidate second device if the study expands. |
| **Plaud NotePin S / Note Pro** | Independent, shipping since 2023 | Reviewers (incl. Plaud's own content — bias noted) rate it the most mature dedicated AI recorder with strong transcription accuracy. Recorder-first rather than always-on-lifelog; different interaction model than Fieldy. |

Category-level observation from multiple reviewers: standalone AI pendants are
consolidating into big-tech platforms (Meta/Amazon buys), with expectations
the concept migrates into glasses/earbuds. Fieldy remaining independent and
opening a developer surface is a differentiator worth noting in study
conclusions.

## Omi in depth (checked against repo + docs, 2026-07-09)

[BasedHardware/omi](https://github.com/BasedHardware/omi): $89 BLE pendant,
MIT-licensed with the full stack published — nRF/Zephyr firmware, Flutter
mobile app, Python/FastAPI backend, macOS desktop app, ESP32-S3 glasses
variant. Active project (~13k stars, 2,100+ forks, v0.12.61 released July
2026). Developer surface is broader than Fieldy's: REST API, Python/Swift/
React Native SDKs, a plugin/app framework, and MCP server support. Repo
claims 24+ h continuous capture — **[inferred/marketing]**, unmeasured, and
this category's hardware claims have already burned us once (see Fieldy RQ4).

**Self-hosting caveat [verified against the backend setup docs]:** a
"self-hosted" Omi backend still *requires* external accounts and keys for
OpenAI, **Deepgram (STT — audio still leaves the network)**, Firebase (auth),
Pinecone, Redis/Upstash, Google Cloud Storage, Pusher, and Hugging Face. The
docs do not cover local substitutes. Out of the box, self-hosting Omi means
running the orchestration layer locally while audio takes essentially the
same cloud path as Fieldy's (Deepgram vs. ElevenLabs; OpenAI either way).
Marketing describes the LLM side as "model-agnostic via OpenAI-compatible
APIs" — pointing it at a local model server may be feasible
**[inferred, unverified]** — but the STT path is Deepgram-coupled; replacing
it with local Whisper would be real engineering, not configuration.

**Study relevance:** Omi's honest advantage is *inspectability*, not privacy.
Fieldy can only be characterized from outside (RQ1–RQ6 exist precisely
because of that); Omi's pipeline is readable code, so a future side-by-side
could separate microphone/hardware quality from cloud-pipeline quality —
impossible in any black-box comparison. Decision as of 2026-07-09: no second
device until Fieldy baselines exist; revisit if Fieldy accuracy or webhook
reliability disappoints.

Additional sources: [Omi backend setup docs](https://docs.omi.me/doc/developer/backend/Backend_Setup),
[Omi docs introduction](https://docs.omi.me/doc/get_started/introduction).

## Methods that fit this study's environment

The homelab already runs Apple Silicon hosts with local LLM tooling, which
makes a **local reference pipeline** cheap to stand up:

- **Reference recorder + local Whisper (adopted as RQ3 control).** A phone or
  lav mic captures the same audio as the Fieldy device; whisper.cpp with
  large-v3 transcribes it locally. Published benchmarks: ~2.7% WER on
  LibriSpeech test-clean, ~8–12% on real-world English; ~2–3× realtime on
  M3/M4-class Apple Silicon with Metal. This gives every accuracy session an
  on-prem baseline — if Fieldy's cloud pipeline (ElevenLabs STT) can't beat a
  local open model on the same audio, that is a headline finding; if it wins
  in noise, that's equally reportable.
- **Whisper large-v3-turbo** trades a small accuracy loss for ~5× speed —
  fine for bulk/spontaneous sessions (script E); use full large-v3 for scored
  takes.
- **Not pursued for now:** buying a second wearable (Omi) for side-by-side —
  worth revisiting after Fieldy baselines exist; open-source hardware would
  let us separate microphone quality from cloud-pipeline quality.

## Sources

- [Plaud: What's the best wearable device for AI note taking? (2026)](https://www.plaud.ai/blogs/articles/whats-the-best-wearable-device-for-ai-note-taking-2026) — vendor content
- [UMEVO: Limitless vs. Bee vs. Omi](https://www.umevo.ai/blogs/ume-all-posts/limitless-vs-bee-vs-omi-the-wearable-ai-showdown) — vendor content
- [UMEVO: Wearable AI wars 2026](https://www.umevo.ai/blogs/ume-all-posts/wearable-ai-wars-2026-limitless-pendant-vs-bee-pioneer-vs-plaud-notepin) — vendor content
- [Forbes: best AI wearables](https://www.forbes.com/sites/forbes-personal-shopper/article/best-ai-wearables/)
- [Big Guy on Stuff: AI wearables 2026 honest review](https://bigguyonstuff.com/ai-wearables-2026-honest-review/)
- [Krisp: best AI note-taking devices 2026](https://krisp.ai/blog/best-ai-note-taking-devices/)
- [VexaScribe: How accurate is Whisper in 2026 (WER data)](https://novascribe.ai/how-accurate-is-whisper)
- [JustVoice: Whisper benchmark on Apple Silicon M1→M4](https://justvoice.ai/blog/whisper-benchmark-apple-silicon-m3-m4)
- [Whisper Notes: Large V3 Turbo vs V3](https://whispernotes.app/blog/introducing-whisper-large-v3-turbo)
- [PromptQuorum: whisper.cpp vs faster-whisper 2026](https://www.promptquorum.com/power-local-llm/local-whisper-stt-comparison-2026)
