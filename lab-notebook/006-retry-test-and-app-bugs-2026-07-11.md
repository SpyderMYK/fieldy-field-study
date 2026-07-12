# 006 — Webhook retry test; app date-label bug

**Date:** 2026-07-11 evening (UTC 2026-07-12).

## RQ1 — delivery semantics: fire-and-forget [verified]

Take-down test: receiver stopped (funnel answering 502), a ~60 s throwaway
conversation spoken and ended manually at 00:38 UTC. Cloud transcription
completed normally (API record "Webhook Retry Test and Technical Update",
00:37:47→00:38:49). Receiver restored 00:43; 45-minute automated watch:
**no redelivery**. The webhook event is permanently absent from our archive.

Consequence (now in [`../data/webhook-schema.md`](../data/webhook-schema.md)):
the webhook is a low-latency hint, not a reliable stream; consumers must
reconcile against the API.

## App observations (screenshot: [`img/006/`](img/006/))

Screenshot taken 18:43 local (00:43 UTC 07-12):

1. **Screen title reads "Yesterday" above today's conversations.** The
   section *bucketing* is correct by local day; only the title is wrong.
   Hypothesis [inferred]: the title compares the section's local date
   against a UTC "today", so every evening after 18:00 Mountain (midnight
   UTC) the app labels today's list "Yesterday". Falsifiable: the label
   should read correctly before 18:00 local and flip at exactly 18:00.
   Same local/UTC confusion family as the server-side timestamp findings.
   Docs-drift/bug tally #7.
2. **The retry-test conversation was absent from the app list** 5 minutes
   after it appeared in the API (screenshot at 18:43; conversation ended
   18:38, API-visible by 18:40). Refresh lag or app/API divergence — soft
   finding, watch for recurrence.
3. **Device battery pill: 100%** — first confirmed full charge. RQ4
   rundown clock starts 2026-07-11 ~18:43 local. (Also 15 s "Testing
   Device Transcription" conversation at 17:29 local — researcher activity
   pre-session; unattributed detail, non-finding.)

## Next

Step 4: offline-storage timestamp experiment (RQ6) — pendant separated
from phone ~15 min, distinctive utterance at an externally noted clock
time, then sync and compare claimed vs. true speech time.
