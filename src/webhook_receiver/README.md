# Webhook capture receiver

Instrument for RQ1 (payload schema, delivery semantics), RQ3 (transcript
content for accuracy scoring), and RQ6 (latency). Captures every request
verbatim to daily JSONL files. Stdlib-only Python; no dependencies.

## Deployment (as running in the study)

- Runs on an always-on Linux host as a systemd service
  ([fieldy-webhook.service](fieldy-webhook.service)), listening on
  `127.0.0.1:8771` only.
- Exposed to Fieldy's cloud via **Tailscale Funnel** on port 8443 —
  `tailscale funnel --bg --https=8443 8771` — so no router ports are
  opened and TLS is handled by Tailscale.
- Auth: Fieldy webhooks carry no HMAC signature, so the receiver requires
  a shared secret in the URL: `https://<host>:8443/?token=<secret>`.
  The token lives in an environment file on the host, not in this repo.
  Unauthorized requests are rejected (403) but still logged headers-only,
  so probe traffic is part of the record.
- Archive lands on ZFS (`/tank/fieldy/raw/webhooks-YYYY-MM-DD.jsonl`),
  covered by automatic snapshots. Raw captures are never committed;
  sanitized excerpts go to `data/`.

## Environment

| Variable | Default | Meaning |
|---|---|---|
| `FIELDY_WEBHOOK_TOKEN` | (required) | shared secret; refuses to start without it |
| `FIELDY_BIND` | `127.0.0.1` | bind address |
| `FIELDY_PORT` | `8771` | bind port |
| `FIELDY_ARCHIVE_DIR` | `/tank/fieldy/raw` | JSONL archive directory |
