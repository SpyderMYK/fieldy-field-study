# 003 — API first contact; timestamp theory

**Date:** 2026-07-10, late evening (UTC 2026-07-11). Continues
[002](002-first-light-2026-07-10.md).

## Done

- API key generated in-app and stored locally off-repo. **Observed:** real
  key prefix is `sk-f-…`, not the documented `sk-fieldy-…` — docs drift #6.
- First authenticated call succeeded. `GET /conversations` characterized —
  contract, item schema, pagination, and the id-only-in-API correlation
  problem written up in [`../data/api-surface.md`](../data/api-surface.md).
- The first-light conversation appears in the API with AI title *"Audio
  Testing with Phonetic Sentences"* and a summary that correctly inferred
  equipment testing/calibration from content alone.

## Key finding — Fieldy's speech timestamps are sync-anchored, not capture-anchored [working theory]

With our clocks NTP-audited, the evidence across webhook + API for one
conversation is only consistent if speech-time metadata is stamped when
audio syncs from pendant to phone, not when spoken (~64–91 s late here).
Server-side fields are honest; speech-time fields are not. Full analysis in
the data docs. Implication for any downstream automation (and for assistive
use): never trust Fieldy's timestamps for when something was said.
Confirmation experiment queued: offline-storage recording with the phone
away should exaggerate the shift to hours.

## Also observed

- Silence-only sessions create "No speech detected" conversation records
  (two today) but fired no webhooks.
- Ongoing capture shows as a record with provisional endTime = start + 3 h;
  the pendant was confirmed still listening after our test ended — ambient
  capture really is continuous once transcribing is started.
- Machine note: this session runs on **herman** (Mac mini M4);
  homelab_state's "(M1)" label for the LabDocs host is stale.

## Addendum — full API surface enumerated (same night)

Found the unauthenticated OpenAPI spec at `api.fieldy.ai/docs/spec.json`.
**RQ2 answered at the documented level: fully read-write** — create/update/
delete on conversations, tasks, speaker profiles, memory templates,
sharables. `GET /transcriptions` is the transcript source (conversation
`content` never populates); segments carry per-segment IDs and a
`source:"live"` field. `GET /user/me` exposes only the account email.
All-segments-identical `createdAt` == webhook `date` further confirms
one-burst ingest at manual end. Details in
[`../data/api-surface.md`](../data/api-surface.md). Practical write test
queued (create→patch→delete on a throwaway object).

## Addendum 2 — MCP connected; LED confirmed; Day 1 checklist complete

- Official MCP server connected to Claude via desktop-app custom connector
  (browser OAuth, account email). Surface: **4 read-only tools** — narrower
  than the REST API by design. Verified round-trip against the first-light
  conversation. Details: [`../data/mcp-surface.md`](../data/mcp-surface.md).
- **LED during active transcription: steady white [verified by direct
  observation]** — matches the LED help article. RQ5 synthesis firming up:
  a recording indicator exists but is an unlabeled white dot, meaningful
  only to someone who has read the vendor's help article; combined with the
  on-box "user's responsibility" disclaimer, Fieldy provides no
  bystander-legible consent affordances.
- The ambient session from tonight closed at exactly its provisional 3-hour
  window with "No speech detected" — continuous ambient capture confirmed.
- **Day 1 checklist: complete** (webhook ✓ API key ✓ MCP ✓ first-light ✓
  LED ✓; permission-screen walk partially documented, to finish).

## Addendum 3 — vendor contacted

Per the pre-registered decision (share after first real data), the
researcher emailed hey@fieldy.ai on 2026-07-10 (local) with the repo link
and a summary of Day 1 findings: the silent no-op button after the
firmware-update BLE orphan, the sync-anchored timestamp evidence, the
docs-drift table — and the positives (quiet-room WER 0, first-try webhook,
developer-friendly validation, read-only MCP surface). Responses, if any,
will be logged here.

**Vendor reply received same evening** (fast enough to suggest an AI support
agent; correspondence paraphrased, not republished). Substance: (a)
recommended re-pairing through the Fieldy app as the supported recovery path
for post-OTA BLE bond breaks — consistent with the troubleshooting article
we followed; (b) **confirmed the API-key docs bug** — docs say `sk-fieldy-…`,
real keys are `sk-f-…` — upgrading that finding from observed to
vendor-acknowledged; (c) requested full payload samples and findings by
email for deeper review of the timestamp offset and docs drift. Follow-up
with samples and server-side identifiers sent in response.

**Second vendor reply:** support agent states the timestamp anchoring is
**not documented internally either** ("our docs don't currently describe how
conversation start/end and segment timestamps are anchored") — so the
sync-anchor theory can't be confirmed or refuted from their support-facing
docs. Their only documented timing behavior: a conversation "may take up to
a couple of minutes to process and finalize" after it ends (consistent with
our observed seconds-scale webhook delivery after manual end). Offered to
route the repo and samples to the appropriate team via a human agent —
accepted; escalation to the developer-platform/firmware side requested.

## Next queue

- MCP server → Claude connection (same account email).
- Enumerate remaining API resources; probe for write verbs (RQ2 core).
- `/conversations/{id}` — does `content` populate?
- LED-during-transcription observation.
- Noisy/TV condition takes (scripts A & C next, then D).
- Offline-storage timestamp experiment.
