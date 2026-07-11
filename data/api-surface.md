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

## Full surface — from the machine-readable spec (found 2026-07-10)

An OpenAPI 3 spec lives unauthenticated at
`https://api.fieldy.ai/docs/spec.json` ("Fieldy Public API", version 2.0.0).
The JS-rendered docs page is just a viewer for it. Endpoint × verb matrix:

| Resource | GET | POST | PATCH | DELETE |
|---|---|---|---|---|
| `/conversations`, `/conversations/{id}` | ✔ list+get | ✔ create | ✔ update | ✔ delete |
| `/tasks`, `/tasks/{id}` | ✔ list | ✔ create | ✔ update | ✔ delete |
| `/transcriptions` | ✔ list | — | — | — |
| `/speaker-profiles`, `/speaker-profiles/{id}` | ✔ | ✔ | ✔ | ✔ |
| `/memory-templates`, `/memory-templates/{id}` | ✔ | ✔ | ✔ | ✔ |
| `/user/me` | ✔ | — | — | — |
| `/sharables`, `/sharables/{id}` | ✔ | ✔ | — | ✔ |

**RQ2 answered (documented surface): the API is fully read-write** —
including `conversations.create`. Write verbs are spec-documented but not
yet exercised; a controlled write test (create → patch → delete on a
purpose-made object) is queued per protocol.

### Verified reads (2026-07-10)

- `GET /user/me` → `{"email": …}` only — minimal account surface.
- `GET /transcriptions?startTime&endTime` → the segment stream. Per-segment
  `id`, `text`, `timestamp`, `speaker`, `speakerProfileId`, `start`, `end`,
  `createdAt`, **`source: "live"`** (implies an offline-storage source
  value — useful for the timestamp experiment).
- `GET /tasks?status=<enum>` — required status filter with lifecycle
  `new|approved|completed|rejected|skipped|cancelled|expired`; empty so far.
- `GET /speaker-profiles` — empty; profiles evidently require enrollment.
- Conversation `content` stayed null in every view tried (`?include=content`
  ignored); **transcript text is only in `/transcriptions` and the webhook**.
- Segment `createdAt` was identical (03:08:10.901) across all six segments
  of the first-light conversation, equal to the webhook `date` — the whole
  conversation ingested server-side in one burst at manual end. Reinforces
  the sync-anchored-timestamps theory.

### Write cycle exercised (2026-07-10, throwaway task)

`POST /tasks` → `PATCH /tasks/{id}` → `DELETE /tasks/{id}`: all worked
first try; deletion verified via list. Observations:

- Task create requires only `title` + `date`; response includes `memoryId`
  (null here) — the task↔conversation linkage field.
- **API-created tasks are born `status:"approved"`** — presumably
  speech-extracted tasks start `new`, giving automations a way to tell
  Fieldy-extracted tasks from API-injected ones. To confirm when script D
  generates real extractions.
- PATCH accepts partial bodies (`required: []`); status transitions and
  completionDate applied without ceremony.

## Still untested

- Rate-limit behavior at the 30 req/min boundary.
- `/transcriptions` pagination and its `source` values for offline captures.
- Write verbs on conversations/speaker-profiles/templates (task cycle
  proven; others presumed similar, verify before relying).
