# Study protocol

**Status:** v1.1, 2026-07-10. The protocol is versioned; changes are logged at the bottom, never silently rewritten.

**Subject device:** Fieldy AI wearable (model/firmware to be recorded on arrival — hardware claims from reviews failed pre-study fact-checking, so nothing is assumed).

**Verification discipline:** every claim in this study is tagged **[verified]** (measured here, or cited to a source we read) or **[inferred]** (reasoning that still awaits a test). Negative results are results and get recorded.

---

## Research questions

### RQ1 — Webhook payload schema and delivery semantics
Fieldy documents *that* webhooks POST every completed transcription, but not the payload schema, retry behavior, or ordering. **[verified: docs silent on all three]**

**Method:** stand up a capture receiver that dumps every request (headers + body) to timestamped JSONL before the device arrives, so payload #1 is captured. Characterize: field inventory across ≥20 payloads, speaker-label format, timestamp semantics, content-type, delivery latency (speech end → POST arrival). Then take the receiver down during a recording and bring it back up to observe retry/replay behavior (count, spacing, give-up point, whether missed events are replayed).

**Deliverable:** `data/webhook-schema.md` + sanitized sample payloads.

### RQ2 — Is the public REST API read-only or read-write?
The API docs (`https://api.fieldy.ai/docs`) are JS-rendered and it is publicly unknown whether writes (create task, edit summary, delete conversation) are supported. **[verified: unknown as of 2026-07]**

**Method:** enumerate documented endpoints, then probe non-destructively with a scoped test account key: `OPTIONS`/documented verbs against each resource. Any destructive-looking test (DELETE) runs only against a purpose-created test conversation. Record the rate-limit behavior at the documented 30 req/min boundary.

**Deliverable:** endpoint × verb matrix in `data/api-surface.md`.

### RQ3 — Real-world transcription accuracy vs. the 95% claim
Vendor claims 95%+ accuracy; reviews report degradation in noise. **[verified: claims exist; magnitudes unmeasured]**

**Method:** scripted readings with known ground-truth text under controlled conditions: (a) quiet room, (b) TV/radio playing in background, (c) two-speaker conversation, (d) outdoor/street. Compute word error rate against ground truth for each condition. Also record whether background-media speech is falsely attributed to a speaker (a known weakness of comparable wearables — Limitless, Omi). All recordings are of the researcher and consenting participants only.

**Deliverable:** WER table by condition, method notes, in `data/accuracy/`.

### RQ4 — Hardware claims verification
The claim set "7-day battery, USB-C, charging case, splash-proof, privacy light, watch/pendant form" was **refuted 0–3** in pre-study fact-checking — reviewers appear to have been describing other devices. **[verified: refuted in fact-check]**

**Method:** on arrival, photograph and record actual form factor, ports, charging mechanism, and any indicator lights. Battery: log charge level daily under normal wear until depletion (no destructive testing; no water testing beyond what the *device's own* documentation states is safe).

**Deliverable:** `data/hardware-actuals.md` with photos.

### RQ5 — Consent and recording-indicator features
~11 US states require all-party consent to record conversations. Does the device/app offer any consent-management, recording-indicator, or multi-party-notification features? **[verified: no source addressed this]**

**Method:** exhaustive walk of device hardware indicators and every app settings screen; check help center for consent guidance. Documented as found/not-found per feature.

**Added in v1.1 — voiceprints as biometrics:** Fieldy's speaker-profiles feature is speaker identification; determine whether vendor docs/privacy policy describe it as voiceprint/biometric collection, and whether any consent, notice, retention, or destruction terms attach to *non-wearer* voices. Context: Illinois BIPA treats voiceprints as biometric identifiers requiring written consent and a destruction policy; Colorado's biometric-consent rules apply to this study's location **[to verify against primary legal sources]**. See `background/ai-notetaker-privacy-context-2026-07.md`.

**Deliverable:** section in `data/hardware-actuals.md` + notebook entry.

### RQ6 — End-to-end pipeline latency
Speech → cloud transcription (ElevenLabs) → webhook POST. No published numbers. **[inferred: expect tens of seconds to minutes, based on "completed transcription" event granularity]**

**Method:** timestamped test utterances vs. receiver arrival times, across ≥10 trials at different times of day.

**Deliverable:** latency distribution in `data/webhook-schema.md`.

---

## Instruments

| Instrument | Purpose | Status |
|---|---|---|
| Webhook capture receiver (Flask, JSONL archive) | RQ1, RQ3, RQ6 | to build pre-arrival |
| API probe scripts | RQ2 | to build |
| Ground-truth reading scripts | RQ3 | to write |
| Official Fieldy MCP server → Claude | qualitative exploration | connect Day 1 |

## Publication rules

1. Notebook entries are append-only and pushed same-day.
2. No raw transcript involving any third party is ever published; payload samples are sanitized (self-recorded or synthetic content, identifiers redacted).
3. Infrastructure internals (LAN/tailnet addresses, hostnames, keys) are redacted from all published material.
4. Findings that reflect poorly on the vendor are published with the same care as favorable ones — this is a study, not a review or an advocacy project.

## Change log

- **v1 (2026-07-08):** initial protocol, pre-arrival.
- **v1.1 (2026-07-10):** RQ5 expanded with voiceprint/biometric sub-question, prompted by AP's 2026-07-09 AI-notetaker privacy report (see `background/ai-notetaker-privacy-context-2026-07.md`).
