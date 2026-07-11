# REST API surface (RQ2) — working notes

Base: `https://api.fieldy.ai/api/public/v2` · Auth: `Authorization: Bearer
sk-f-…` (n.b. real key prefix is `sk-f-`, not the `sk-fieldy-` the help
docs describe). Documented rate limit 30 req/min (not yet probed).

## GET /conversations — characterized 2026-07-10

- **Required** query params: `startTime`, `endTime` (ISO-8601 strings; a
  bare request returns a structured 400 with per-field issues — validation
  errors are developer-friendly).
- Returns `{items: [...], nextCursor}` (cursor pagination; nextCursor null
  on single page).
- Item schema observed:
  `id` (UUID), `title`, `summary` (AI-generated), `content` (null in list
  view), `startTime`/`endTime`, `type: "FULL"`, `keywords[]`, `speakers[]`,
  `memorySpeakers[]`, `quotes[]`, `location` (null) + `locationId` (set!),
  `templateId`, `memoryTemplateId`, `recommendedTemplateIds`,
  `calendarEventId`, `updatedAt`.
- **Webhook↔API correlation:** the webhook payload carries no `id`, so
  linking a webhook event to its API record requires time/content matching.
- Silence sessions ("No speech detected") produce conversation records but
  **no webhook events** (n=1 basis).
- An **ongoing** capture session appears as a record with a provisional
  endTime exactly +3 h from startTime.

## Timestamp reliability (cross-checked with webhook + NTP audit)

Local clocks verified against NTP (alien 0.0004 s, herman 0.034 s off).
For the first-light conversation, server-side fields (webhook `date`,
API `updatedAt`) sit at true time, but speech-time fields (conversation
`startTime`/`endTime`, segment `timestamp`s) run **~64–91 s later than the
speech physically occurred** — the full transcript arrived at our receiver
before the API's claimed conversation end.

**Working theory [inferred]:** speech-time metadata is anchored to
pendant→phone sync time, not capture time; the shift equals the BLE sync
lag. Test: offline-storage recording (phone absent) should shift these
fields by hours.

**Consequence:** downstream automations must not trust Fieldy's speech
timestamps for time-of-utterance semantics; anchor externally (spoken
slate + local clock, or timecode reference recorder).

## Untested

- Other resources (tasks, speaker profiles, templates, sharable links,
  user info) — endpoints not yet enumerated.
- Whether any write verbs exist (RQ2 core question).
- Rate-limit behavior at the 30 req/min boundary.
- Fetching a single conversation by id (presumably `/conversations/{id}`)
  and whether `content` populates there.
