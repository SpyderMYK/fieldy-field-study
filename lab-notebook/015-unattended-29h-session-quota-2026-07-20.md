# 015 — Unattended 29-hour session consumed the entire monthly quota

**Date:** 2026-07-20. The most consequential finding of the study so far.
No third-party conversation is involved (the captured audio was a broadcast
radio station), so this entry describes the event directly.

## What happened

A single continuous transcription session ran from **2026-07-19 14:20 UTC to
2026-07-20 19:44 UTC — 29 h 24 m**. Its captured content was a **broadcast
radio station** (music, vocals, DJ segments, station promos) playing in the
researcher's home. Fieldy transcribed the entire span and generated an AI
summary of it as though it were a conversation.

**The researcher was not aware the device was transcribing during this
period.**

## Consequences

1. **The entire monthly transcription quota was consumed.** ~29.4 h =
   **~1,764 transcription minutes**. Published plans: **Free 150 min/mo,
   Plus 1,440 min/mo, Unlimited**. So this single unattended session
   **exceeded even the paid Plus tier's full monthly allowance**, and is
   ~12x the free tier. The researcher discovered it only by running out of
   minutes.

2. **~29 hours of household ambient audio was uploaded and processed in the
   cloud** (Fieldy's pipeline transits third-party STT/LLM services) without
   the user's awareness. This is a privacy exposure, not merely a billing one.

3. **The vendor's stated protection did not apply.** Fieldy's documentation
   states transcription minutes are *"counted only when voice is detected;
   any background noise or chatter will not count towards used minutes."*
   A radio broadcast **is** voice — singing, speech, promos — so it passed
   the voice-detection gate and billed as conversation. The protection a user
   would reasonably infer from that wording **does not cover broadcast
   audio**.

4. **No way to monitor or guard against it programmatically.** The public API
   exposes **no usage/quota/plan endpoint** (verified against the live
   OpenAPI spec: only conversations, tasks, transcriptions, speaker-profiles,
   memory-templates, user/me, sharables; `/user/me` returns only an email).
   A developer cannot check remaining minutes or build an automated stop.

## Cause — stated honestly

Two explanations fit the evidence and **this data cannot distinguish them**:

- **(a) A session was started and never stopped.** Consistent with prior
  characterization (notebook 003): capture is continuous once "Start
  Transcribing" is pressed, and an ongoing session appears as a record with a
  rolling provisional end time. Under this reading the device did exactly
  what it was told — but there is **no auto-stop for a long unattended
  ambient session, and no persistent, hard-to-miss indication that it is
  still running** (the only signal is a small steady-white LED, invisible if
  the pendant is set down, in a pocket, or in another room).
- **(b) Transcription began without the user initiating it.** No evidence
  supports this over (a), and (a) is the more probable reading. Recorded
  only so the record is complete.

Either way the user-facing outcome is identical: **a day and a half of
recording the user did not know was happening.**

## Why this matters beyond one user's bill

This is the same root cause as the TV-contamination finding (notebook 004) —
the device cannot distinguish a person in the room from a loudspeaker in the
room — but here it carries **financial and privacy** consequences rather than
just a polluted transcript. It also compounds RQ5 (consent): **if the wearer
himself did not know it was recording, bystanders certainly did not.**

## Suggested fixes (for vendor feedback)

- Auto-stop or prompt after N hours of continuous/unattended capture.
- Don't bill (and ideally don't transcribe) audio classified as broadcast
  media rather than live conversation.
- Expose usage/quota in the public API so integrations can self-limit.
- A clearer persistent "still recording" signal (push notification after
  prolonged capture, not just an LED).

## Researcher's position

The researcher considers this serious enough to reconsider continued use of
the device. Logged here as a study finding regardless of that decision.
