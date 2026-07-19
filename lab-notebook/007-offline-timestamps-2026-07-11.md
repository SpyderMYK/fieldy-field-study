# 007 — Offline-storage experiment: sync-anchor theory refuted, replaced

**Date:** 2026-07-11 night (UTC 2026-07-12). RQ6.
Sample: [`../data/samples/payload-004-offline-storage.json`](../data/samples/payload-004-offline-storage.json).

## Design

Pendant separated from phone (~9:08–9:41 PM local, out of BLE range,
LED steady white throughout — the documented offline-storage state). At an
externally noted clock time the researcher spoke a self-timestamping line.
Reunited and synced at ~9:41 PM.

## Ground truth vs. claims

| Quantity | Value (UTC) |
|---|---|
| True utterance time (spoken, self-timestamping) | 03:27:25 |
| Claimed segment timestamp | 03:29:16.8 (**+1 m 52 s**) |
| Sync/ingest (`createdAt`, webhook receipt) | 03:41:24 (+14 min after speech) |
| Conversation record | 03:08:17.8 → 03:41:49.8 |

## Findings

1. **Sync-anchor theory (entry 003) REFUTED.** A 14-minute sync delay did
   NOT shift the claimed speech time. The lateness stayed ~2 minutes —
   the same magnitude observed over live BLE. Recorded as designed: the
   experiment was built to break the theory, and it did.
2. **Replacement theory [inferred]:** a roughly constant ~1–2 minute
   lateness in speech-time metadata, from either (a) a late-stamped
   conversation-start anchor with honest audio offsets, or (b) honest
   anchor with inflated offsets. Discriminating test queued: speak a time
   hack immediately after tapping Start.
3. **Engineering upshot — better than feared:** timestamp error appears
   *bounded* (~2 min) rather than unbounded-by-sync-delay. Automations can
   treat Fieldy speech times as ±2 min, regardless of offline duration.
4. **`source` stays `"live"` for offline-stored captures** — it does not
   mark offline provenance. The offline signature is burst `createdAt`
   equal to sync time.
5. **Offline speech is labeled `"Unknown"`** rather than "Speaker 1" —
   the offline path diarizes differently.
6. **No hallucinated content**: ~21 minutes of silent walking produced
   exactly one segment (the spoken line). The webhook fired seconds after
   sync completed.
7. LED: steady white for the entire separated period [verified, direct
   observation] — matches the LED article's offline-storage state.

## Session wrap (2026-07-11)

Tonight: TV condition (004), numbers/jargon (005), retry test + app bugs
(006), offline timestamps (007). Remaining queue: script D two-speaker
take, anchor-discrimination time-hack take, battery rundown (running),
"Yesterday" title-flip check at 18:00 local, permission-screen walk.

## Addendum — vendor escalation confirmed (2026-07-12)

Named support agent (Justin) confirmed the full package — timestamp
analysis, payload notes, repo links — was passed to the team handling the
developer platform and device firmware; they will reach out after review.
Correspondence continues to be paraphrased, not republished. (Incidental:
Fieldy's email footer reads "Previously Compass" — prior company name,
noted for background.)

## Addendum — Fieldy team reached out; call being scheduled (2026-07-18)

The escalation landed with a real result: a member of the Fieldy team
(Adomas) emailed on 2026-07-15 saying he was impressed by the study and
asking to hop on a call this week, then followed up on the 18th. Researcher
replied to schedule. So the study went full circle — findings published →
support triage → dev/firmware team → a direct conversation with the vendor.
Correspondence paraphrased, not republished. Any product/technical outcomes
from the call that are non-confidential will be logged here.
