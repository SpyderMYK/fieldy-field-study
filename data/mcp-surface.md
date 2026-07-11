# Official MCP server surface — verified live 2026-07-10/11

Endpoint `https://api.fieldy.ai/mcp`, connected to Claude via the desktop
app's custom-connector flow; browser OAuth against the account email.

## Tools exposed (complete list)

| Tool | Function |
|---|---|
| `fieldy_list_recent_conversations` | reverse-chron catalog, cursor pagination |
| `fieldy_list_conversations_in_time_range` | half-open ISO interval, ≤30-day window |
| `fieldy_get_conversation` | full record by id |
| `fieldy_list_transcripts` | raw segment stream by time range, ≤7-day window |

## Observations

- **Read-only by design**: no task, template, speaker-profile, sharable, or
  any write tools — a deliberately narrower surface than the REST API's
  full CRUD (see [`api-surface.md`](api-surface.md)). Credit where due.
- Tool errors document **granular OAuth scopes** (`conversations:read`,
  `transcripts:read`).
- Tool descriptions are unusually well-written (use/don't-use guidance,
  pagination and error contracts, explicit "no full-text search exists").
- Verified round-trip: listing returned the first-light conversation with
  identical fields to the REST API — same records, same timestamps (and
  therefore the same sync-anchored timestamp caveat).
- First-connection UX: tools appeared in an already-running Claude session
  immediately after OAuth completed; no restart needed.
