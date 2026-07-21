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

---

# CORRECTION (same day) — the 29-hour figure was WRONG

The researcher challenged the premise: he was in the room the whole period
and would have noticed the recording LED. That prompted checking the
underlying transcript segments instead of the reported duration. **He was
right and the analysis above was wrong.**

**Measured:** the "29-hour" conversation contains only **38 transcript
segments spanning 62.4 minutes** (2026-07-19 14:22:24 → 15:24:48, 349
words). There are **no segments at all** for the remaining ~28 hours.

**So:** the device captured **~1 hour** of radio audio, not 29 hours. The
conversation's reported `endTime` (2026-07-20T19:44:03) is **exactly the
`startTime` of the next session** (the lunch conversation) to the second —
i.e. Fieldy stretched the record to fill the gap until the next session
began.

### What is retracted

- ~~1,764 transcription minutes consumed by one session~~ — **false**.
  Actual captured audio ≈ **62 minutes**.
- ~~A single session exceeded even the paid Plus tier's monthly allowance~~
  — **false**.
- ~~29 hours of household ambient audio uploaded unnoticed~~ — **false**;
  roughly one hour was.
- The alarming framing of "a day and a half of recording you didn't know
  about" is withdrawn. The device was very likely on, with its LED lit, for
  about an hour.

### What still stands

1. **Broadcast audio is transcribed and does bill against the quota.**
   ~62 minutes of a radio station were transcribed and summarized as a
   "conversation" — ~41% of the 150-min free tier from one hour of music.
   The vendor's *"background noise or chatter will not count"* wording still
   does not protect against broadcast **voice**. Same root cause as the TV
   finding (notebook 004).
2. **No usage/quota endpoint in the public API** (re-verified) — users and
   integrations cannot monitor remaining minutes.
3. **Quota exhaustion is explained by cumulative study usage**, not one
   runaway session: the radio hour (~62 m) plus the meeting (~53 m), lunch
   (~27 m), field walk (~24 m) and assorted tests comfortably exceeds the
   150-minute free tier.

### NEW finding surfaced by the correction

**Fieldy reports grossly inflated conversation durations.** A conversation
holding 62 minutes of audio is reported as spanning **29 h 24 m** — ~28x
the real content — because the end time runs to the start of the next
session rather than the end of captured audio. Any user reading the app (or
the API) would badly misjudge both their recording history and their usage.
This is a reporting/data-model bug, and a more defensible thing to raise
with the vendor than the retracted alarm above.

### Method lesson (third time)

Fieldy's own reported time fields have now misled this study three times.
**Never infer duration or usage from Fieldy's reported timestamps — always
verify against the underlying transcript segments.**

---

## Ambiguity resolved — it is a reporting artifact [verified by placement]

The correction above left two readings open: (a) a reporting artifact, or
(b) the device genuinely powered and capturing for ~29 hours with only ~62
minutes of voice. Note that (b) could not be dismissed on the "end time ==
next session's start" signature alone, since a continuously-recording device
split into consecutive conversations would produce exactly that.

**Resolving evidence (researcher's physical setup):** the pendant lives
permanently hanging at the researcher's desk, **inside his peripheral vision
from his working position**, and the LED is plainly noticeable when lit. The
29-hour span covers **many waking hours the researcher spent at that desk**
(afternoon/evening of the 19th, morning of the 20th). No lit LED was
observed at any point in those hours. Overnight hours were unobserved, but
the daytime hours alone are sufficient — a continuously-lit 29-hour session
could not have gone unnoticed.

**Conclusion: (a) — the device was NOT capturing for 29 hours.** It ran for
roughly the one-hour radio period and then stopped; Fieldy's reported
conversation `endTime` stretched to the start of the next session ~28 hours
later.

**So the standing finding is the reporting bug, and it is user-facing:**
Fieldy reports a conversation duration ~28x longer than the audio it
actually contains (29 h 24 m reported vs 62 min captured), and **the app
displays the same inflated span**, not just the API. A user reading their
own history will badly misjudge how long the device was recording — which is
precisely the false alarm this notebook entry itself fell into.

No privacy incident occurred. The device behaved as instructed and its
indicator worked as designed; the defect is in duration reporting.
