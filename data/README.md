# Data

Measurement data, payload samples, and schema notes produced by the study.

**Everything in this directory is sanitized before commit:**

- Payload samples contain only self-recorded or synthetic speech content.
- Account identifiers, conversation IDs, API keys, and tokens are redacted or replaced with obvious placeholders (`sk-fieldy-REDACTED`, `conv_EXAMPLE`).
- Infrastructure details (LAN/tailnet addresses, hostnames) are redacted.
- Raw unsanitized captures live outside this repository (`data/raw/` is gitignored as a guard, but the working rule is that raw captures never enter the repo tree at all).

Planned contents (see [protocol](../protocol/study-protocol.md)):

- `webhook-schema.md` — RQ1/RQ6: payload field inventory, delivery & retry semantics, latency
- `api-surface.md` — RQ2: endpoint × verb matrix
- `accuracy/` — RQ3: ground-truth scripts and WER results by condition
- `hardware-actuals.md` — RQ4/RQ5: measured hardware reality + consent-feature findings
