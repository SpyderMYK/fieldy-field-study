# src

Tools built for the study (MIT licensed).

Planned:

- `webhook_receiver/` — minimal Flask capture server: logs every POST (headers + body) to timestamped JSONL, token-checked via URL query param (Fieldy webhooks have no HMAC signing)
- `api_probe/` — RQ2 endpoint enumeration and non-destructive verb probing, rate-limit aware (30 req/min)
- `analysis/` — WER computation for RQ3, latency stats for RQ6

Secrets (API keys, webhook tokens) are read from environment/local config — never committed.
