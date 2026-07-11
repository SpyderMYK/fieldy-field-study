# Webhook payload schema (RQ1) & delivery notes (RQ6)

Working characterization from live captures. Sample payloads in
[`samples/`](samples/) (sanitized: our hostname redacted; content is
researcher-scripted speech). n=1 so far — everything here is provisional.

## Transport

- One POST per completed conversation (first light: a 71-second, 6-segment
  conversation arrived as a single POST — no per-segment streaming).
- `Content-Type: application/json`; sender `User-Agent: python-httpx/0.28.1`;
  egress IP 152.55.180.114 on first capture.
- No signature/HMAC headers of any kind (confirms docs). Auth is entirely
  whatever the user embeds in their URL.
- Arrives via HTTPS; query string carried our token (receiver logs the path
  only, so tokens don't sit in the archive).

## Body schema (as observed, v3.3.4-era backend)

```json
{
  "date": "<ISO-8601 UTC — send time (matches receipt within ~0.4 s)>",
  "transcription": "<full conversation text, newline-joined>",
  "transcriptions": [
    {
      "text": "<segment text, punctuated>",
      "speaker": "Speaker 1",
      "start": 3.39,        // seconds from conversation start
      "end": 7.47,
      "timestamp": "<ISO-8601 UTC — see anomaly below>"
    }
  ]
}
```

### Notable absences

- **No conversation ID** — correlating a webhook event with an API
  `/conversations` record requires content/time matching (RQ2 to-do).
- No event type, no user/device ID, no summary, no extracted tasks —
  transcription only (consistent with docs).
- **No wearer designation**: all segments were `Speaker 1` even though the
  background report describes the wearer as "distinctly marked." Two-speaker
  takes (script D) will show what labels non-wearers get.

## Timestamp anomaly (first capture — resolved to a working theory)

Payload received at alien 03:08:11.35 UTC; Fieldy's own `date` field agrees
(03:08:10.94). But the segment `timestamp` fields run to 03:09:04 — **~53 s
after the payload was received** — and the API record for the same
conversation claims endTime 03:09:36 with `updatedAt` 03:08:13 (a record
"last updated" 83 s before it ended).

Receiver-side clocks were audited against NTP (alien 0.0004 s off,
chrony stratum 3; herman 0.034 s off) — the inconsistency is Fieldy's.

**Working theory [inferred]:** server-side fields (webhook `date`, API
`updatedAt`) are true wall-clock; speech-time fields (segment `timestamp`s,
conversation `startTime`/`endTime`) are anchored to pendant→phone **sync**
time and sit late by the BLE sync lag (~64–91 s here). See
[`api-surface.md`](api-surface.md) for the cross-check and the
offline-storage test that would confirm it.

Working rule: **treat `start`/`end` offsets as meaningful, absolute
speech timestamps as unreliable.** RQ6 latency measurement requires an
externally logged speech time (slate at a noted clock second, or a
timecode reference recorder).

## Delivery semantics

- First light: conversation ended manually in-app; payload observed in the
  archive within seconds-to-a-minute of the manual end (exact latency
  pending the anomaly above).
- Retry behavior on receiver downtime: untested (planned: RQ1 take-down
  test).

## RQ3 first datapoint (quiet room, scripted)

Harvard set 1 via pendant on lanyard, quiet room: **all ten sentences
word-perfect** (WER ≈ 0 excluding the slate word under review). Punctuation
and quote marks inserted sensibly. Numbered list spoken as words rendered
as words.
