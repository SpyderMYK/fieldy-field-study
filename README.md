# Fieldy Field Study

An open, empirical study of the [Fieldy](https://www.fieldy.ai/) AI wearable: what the device and its developer surface actually do, measured and documented in public.

**Researcher:** Mike Spille ([@SpyderMYK](https://github.com/SpyderMYK))
**Research & administrative assistants:** Claude (Anthropic)

## Why

Fieldy ships with a real but quietly documented developer surface — webhooks, a REST API, and an official MCP server — none of which appears on the marketing site. Meanwhile some marketing claims (hardware specs, "on-device processing") failed independent fact-checking during our background research. This study tests the device against its claims and characterizes the undocumented parts of the developer surface, in the open, so other builders don't have to rediscover it.

Findings are shared with the Fieldy team and published here as they happen.

## Structure

| Path | Contents |
|---|---|
| [`protocol/`](protocol/) | Research questions, methodology, and the Day 1 checklist |
| [`lab-notebook/`](lab-notebook/) | Dated entries documenting every session — observations, raw notes, dead ends included |
| [`background/`](background/) | Pre-arrival deep-research report (100-agent sweep, top 25 claims adversarially fact-checked) |
| [`data/`](data/) | Sanitized payload samples, schema notes, measurement data |
| [`src/`](src/) | Tools built during the study (webhook receiver, API puller, analysis scripts) |

## Method

Every claim in this repo is tagged **verified** (we measured it or cite a source) or **inferred** (reasoning, awaiting test). Notebook entries are append-only: mistakes and negative results stay in the record.

## Ethics & privacy

- Raw audio and transcripts involving anyone other than the researcher are **never** published. Payload samples in `data/` are sanitized (synthetic or self-recorded content only, identifiers redacted).
- All test recordings during the study are of the researcher or of consenting participants.
- Homelab infrastructure details (addresses, hostnames, credentials) are redacted from published material.

## License

Code in `src/` is [MIT](LICENSE). Everything else (protocol, notebook, reports) is [CC BY 4.0](LICENSE-docs.md) — reuse freely with attribution.
