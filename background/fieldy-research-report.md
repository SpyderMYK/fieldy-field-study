# Fieldy AI Wearable — Integration Research Report

**Date:** 2026-07-08 (device arriving 2026-07-09)
**Method:** Deep-research sweep (100 agents; vendor docs, GitHub, reviews, adjacent-wearable ecosystems). 90 claims extracted, top 25 adversarially fact-checked with 3-vote verification: 24 confirmed, 1 refuted.

---

## TL;DR

Fieldy has a real, free, officially documented developer surface — **webhooks, a REST API, and an official MCP server** — even though the marketing site mentions none of it (it's all in the help center). The device is phone-tethered and cloud-processed; there is no local/offline AI. The community ecosystem is young and thin: one flagship integration exists (the OpenClaw `fieldy-ai-webhook` skill), and the Limitless Pendant ecosystem provides the best portable patterns. No verified prior art exists for assistive (dementia/elderly) deployments — that space is open.

---

## 1. What the device is

- **Architecture:** records audio on-device (Fieldy 3 buffers up to ~3 days offline), but ALL transcription and AI runs in the cloud. Backend on Google Cloud (US); speech-to-text by **ElevenLabs**; AI features by **OpenAI**. Phone app must be open with internet to sync. No local processing mode exists — marketing mentions of "on-device processing" are contradicted by Fieldy's own privacy policy.
- **Features (confirmed by docs + independent reviews):** real-time transcription (claimed 95%+ accuracy, drops in noise), 100+ languages, instant summaries, automatic task/reminder extraction from speech, AI chat over past conversations, desktop-app recording of online meetings, customizable summary templates ("My Templates"), speaker profiles (wearer distinctly marked; others labeled A–E).
- **Known complaints:** app sync/stability issues, accuracy degradation in noisy environments.
- ⚠️ **Hardware specs unverified:** the claim set "7-day battery, USB-C, charging case, splash-proof, privacy light, watch/pendant form" was REFUTED 0–3 in fact-checking. Check the physical device rather than trusting reviews.

## 2. Integration surfaces (all verified live July 2026)

### Webhooks (push) — free, all users
- Setup: app → **Settings → Developer Settings** → paste URL. Delivery starts automatically.
- POSTs every completed transcription. Transcription events only; no event filtering.
- **No HMAC/signing** — embed your own token in the URL query string.
- Retry/delivery semantics undocumented. Fieldy calls it "basic functionality for now."
- Docs: https://intercom.help/fieldy/en/articles/11186620-webhooks-for-developers and https://fieldlabsinc.github.io/docs/#/webhooks

### REST API (pull)
- Base: `https://api.fieldy.ai/api/public/v2`
- Auth: bearer keys `sk-fieldy-...` generated in Developer Settings. Rate limit 30 req/min.
- Resources: conversations (summaries, content, timestamps, location, keywords, quotes), timestamped speaker-labeled transcripts, tasks, speaker profiles, memory templates, sharable links, user info.
- Docs: https://api.fieldy.ai/docs (JS-rendered). Unknown whether writes are supported.

### Official MCP server
- Endpoint: `https://api.fieldy.ai/mcp` — browser OAuth (same email as the app; Apple Private Relay users must use the relay email).
- Works with Claude Desktop/Code, ChatGPT, Cursor.
- Docs: https://intercom.help/fieldy/en/articles/15019124-connecting-fieldy-to-claude-chatgpt-and-your-own-apps

### Zapier / IFTTT
- No native app in either directory. Fieldy's docs route Zapier via "Webhooks by Zapier" (Catch Hook trigger) → Google Sheets / Slack / Email.

## 3. What others have built

- **Flagship:** `fieldy-ai-webhook` skill for **OpenClaw** (formerly Moltbot/Clawdbot), documented on Fieldy's own blog. Gives a "Hey, Fieldy" spoken wake word forwarded as a command to a self-hosted agent; all other transcripts archived to local JSONL under `<workspace>/fieldy/transcripts/`. Wake-word regex is user-editable in `fieldy-webhook.js`. Install verified working: `npx molthub@latest install fieldy-ai-webhook`. Guide: https://www.fieldy.ai/blog/fieldy-ai-webhook-moltbot-clawdbot-guide (community author: mrzilvis on ClawHub).
- **Portable patterns from Limitless Pendant ecosystem** (same cloud-API architecture):
  - https://github.com/BurtTheCoder/mcp-limitless (now maplehilllabs/mcp-limitless) — Claude search/retrieve/analyze over lifelogs.
  - https://github.com/ipvr9/mcp-limitless-server (MIT) — five-tool template: get-by-id, list-by-date, list-by-range, list-recent, text search.
- Beyond these, almost nothing Fieldy-specific survived fact-checking — Reddit/HN/Discord/YouTube write-ups are scarce. The developer surface is only a few months old (webhook article Apr 2026, MCP article May 2026); expect it to evolve, possibly with breaking changes.

## 4. Project ideas

### Week-one starters (in order)
1. **Day 1, zero code:** add the MCP server to Claude; generate an API key. Ask Claude about your day — immediately reveals real transcript/speaker-label quality.
2. **Webhook receiver on a Pi:** ~20-line Flask/Express server dumping every payload to JSONL. The foundational project — characterizes the (undocumented) payload schema and delivery reliability, and becomes the local archive everything else builds on.
3. **API puller:** cron script hitting `/conversations` and `/tasks`, diffing against the archive. Tests the pull path and rate limit.
4. **"Hey, Fieldy" wake word:** via the OpenClaw skill, or roll your own regex on the webhook stream piped to any agent.

### Ambitious builds
- **ADHD — end-of-day review agent:** pull the day's conversations, extract verbal commitments ("I'll send that Tuesday"), deliver a digest with Fieldy's auto-extracted task list.
- **ADHD — commitment catcher:** near-real-time webhook trigger when a promise is spoken → Reminders / task system.
- **Morning briefing:** "here's what you said yesterday."
- **Caregiver daily summary:** generated from the transcript stream, pushed to family.
- **Dementia conversation recall:** "what did the doctor say?" over the archive.
- **CRM/notes sync** via the REST API.

## 5. Assistive use — caveats

- **No verified prior art** for Fieldy or comparable-wearable deployments with dementia/elderly users. Pioneering territory.
- **Consent:** ~11 US states require all-party consent to record conversations. A dementia patient's *capacity to consent* — as wearer or recorded party — is a genuine legal/ethical question no source addressed. Aides, visitors, and doctors get recorded too.
- **Data path:** audio transits ElevenLabs and OpenAI. "HIPAA compliant," "no audio stored," and "E2E encryption" claims are vendor-self-declared with no published third-party audit — and HIPAA doesn't straightforwardly apply to family caregivers anyway. "No audio stored" addresses retention, not transmission.
- **Practical:** comparable wearables (Limitless, Omi) cannot distinguish real conversation from a TV in the background — significant in an elderly household.
- **Recommended path:** prototype everything on yourself first; the webhook → local-JSONL pattern keeps downstream processing on the homelab rather than adding more clouds.

## 6. Open questions to test on the device

1. Exact webhook payload schema (fields, speaker labels, timestamps) and delivery/retry semantics when the receiver is down.
2. Is the public API read-only, or can automations write back (create tasks, edit summaries, delete conversations)?
3. Real-world transcription accuracy, battery life, and app stability (hardware marketing claims failed fact-check).
4. Does Fieldy offer any consent-management, recording-indicator, or multi-party-notification features?

## Key sources

- https://www.fieldy.ai/ and https://www.fieldy.ai/policy/privacy-policy
- Help center: webhook, MCP/API, tasks, and templates articles at intercom.help/fieldy
- https://fieldlabsinc.github.io/docs/ (developer docs)
- https://www.fieldy.ai/blog/fieldy-ai-webhook-moltbot-clawdbot-guide
- https://api.fieldy.ai/docs
- Reviews: unite.ai, cybernews.com, Trustpilot, Product Hunt ("Can this AI wearable help my ADHD brain…")
- Limitless patterns: github.com/BurtTheCoder/mcp-limitless, github.com/ipvr9/mcp-limitless-server

---
*Generated by Claude Code deep-research workflow, 2026-07-08. Fact-check votes and full agent transcripts in session archive.*
