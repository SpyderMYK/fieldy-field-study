# 016 — An unattended 3-hour recording: auto-start investigation

**Date:** 2026-07-20 (analysis the same night, UTC 2026-07-21).
Companion to [015](015-unattended-29h-session-quota-2026-07-20.md), which
this entry both corrects and independently confirms.

## The event

A recording ran for **exactly three hours** on the researcher's device, and
**no user action started it.**

| Field | Value |
|---|---|
| Conversation id | `aa139733-a3e3-5f15-95ea-d7b098cccdc4` |
| `startTime` | 2026-07-20T22:05:21.747Z (16:05 local, MDT) |
| `endTime` | 2026-07-21T01:05:21.618Z (19:05 local) |
| Elapsed | **2 h 59 m 59.871 s** |
| `title` / `summary` | "Recording saved" / saved but not transcribed |
| Transcript segments | **0** (quota exhausted — recorded, not transcribed) |
| `locationId` | present (home; distinct from that day's restaurant record) |

**Researcher's position during the event [verified — direct account]:** at his
desk from before 16:05 until 18:20 (**2 h 15 m of the recording**), with the
pendant hanging in its usual place on a microphone stand, inside his
peripheral vision. Away from the room 18:20–19:05. He pressed nothing, and
did not know a recording was running until reviewing the app that evening.

## Finding 1 — the *stop* is fully explained: a documented 3-hour cap [verified]

`endTime − startTime` = **2:59:59.871** — three hours minus 129 ms. That is a
computed ceiling, not a real-world event, and Fieldy's own Fieldy 3 guide
documents it: each conversation can run up to three hours, and the device
stops automatically at the limit.

So the recording did not "decide" anything about the empty room. It ran until
it hit a documented maximum.

**This independently confirms notebook 015.** If sessions cap at three hours,
the "29 h 24 m" jazz record *cannot* have been continuous capture — it would
have been cut off after three. 015's conclusion (the 29-hour span is an
end-time reporting artifact, not 29 hours of recording) now rests on a second,
stronger foundation than the LED-observation argument it originally used.

## Finding 2 — recording continues after the transcription quota is exhausted [verified — NEW]

With the free tier's 150 minutes spent, **the device keeps recording.** The
app lists such sessions as "Recording saved" with a lock icon and a
**"Transcribe"** button; the API returns them as ordinary conversations with a
summary saying the recording is saved but not transcribed, and zero segments.

Capture is **not** gated by quota — only *reading your own audio* is. Two
consequences worth stating plainly:

1. **Running out of minutes is not a safety limit.** A user who believes an
   exhausted quota means the device has stopped listening is wrong.
2. **Audio accumulates in the vendor's possession that the user cannot read
   without paying.** That is a defensible product decision, but it deserves to
   be explicit rather than discovered.

## Finding 2b — untranscribed recordings emit **no webhook** [verified]

The study's webhook receiver has run continuously since 2026-07-15 (Tailscale
Funnel confirmed up, no outage in the logs). On the day of the event it fired
exactly twice, and **the two events are not what they first appeared to be**:

| Received | Segments | Which conversation |
|---|---|---|
| 20:11:19.858Z | 354 | the lunch (171+180+3 = 354, notebook 014) |
| 20:13:10.163Z | **38** | **the jazz** (38 segments, notebook 015) |

*(An earlier revision of this entry asserted both events were the lunch. That
was wrong — corrected on the researcher's challenge, "what about the webhook
for the 29-hour session?" See Finding 2c, which that question uncovered.)*

**No webhook was received for the 3-hour recording**, and none after 20:13Z.
The conclusion stands on the 3-hour recording alone: **it was never
transcribed, and it produced no webhook.**

So the webhook fires on *transcription* completion, not on *recording*
completion. Practical consequence for anyone building on this: **while a user
is over quota, the webhook path cannot see their activity at all.** Capture
continues (Finding 2), but the integration surface goes silent — the one
combination where an external monitor would be most useful is the one that
does not report. Detecting these requires polling the conversations endpoint.

## Finding 2c — the 29-hour session is now **fully** explained: a 29-hour offline hold [verified]

Chasing the jazz webhook produced the mechanism that notebook 015 was missing.

All **38** jazz segments carry a **single identical** `createdAt` —
`2026-07-20T20:13:09Z` — matching the webhook received at 20:13:10.163Z. The
audio itself was spoken 2026-07-19 14:22–15:24Z.

**Burst `createdAt` equal to sync time is the offline-storage signature this
study characterised in [notebook 007](007-offline-timestamps-2026-07-11.md).**

So the sequence was:

1. **07-19 ~14:20Z** — a session begins; ~62 min of broadcast radio is captured.
2. The pendant is **not synced to the phone**; the audio sits in offline storage
   and the conversation record stays **open**.
3. **~29 hours pass** with the audio unsynced and the record unclosed.
4. **07-20 19:44:03Z** — the lunch session begins. Fieldy closes the stale open
   record *at that boundary*, which is why its `endTime` is exactly the next
   session's `startTime` — the signature 015 spotted but could not explain.
5. **07-20 20:13:09Z** — everything flushes: 38 segments ingested in one burst,
   webhook delivered one second later.

**The device was not recording for 29 hours.** Three independent lines now
agree: only 62 minutes of audio exist (015), a 3-hour cap makes 29 hours
impossible (Finding 1), and the ingest burst shows a 29-hour *hold*, not a
29-hour capture (here).

**The real defect is therefore sharper than "inflated durations":** an
unsynced session stays open indefinitely, and its reported duration silently
becomes *time-until-next-sync* rather than time recorded. Any user whose
pendant goes unsynced overnight will see a fictitious multi-hour conversation
in their history. That is a concrete, reproducible bug with a clear fix (close
a session at the end of its captured audio, not at the next session's start).

## Finding 3 — hypotheses tested and eliminated

Every plausible trigger was tested. All failed.

| Hypothesis | Test | Result |
|---|---|---|
| Reconnection triggers auto-start | Bluetooth off ~30 s, back on | **No recording, no LED** [verified] |
| Accidental activation (bumped stand) | Researcher's standing experience | Bumping, even roughly, does not activate [verified] |
| Single click starts capture (per marketing) | Direct, long-standing use | Single click = brief status blink only [verified] |
| Capture came from the phone's microphone | Vendor docs | No such mode; pendant is the sole mic [verified] |
| Siri / Shortcuts triggered it | Search of integrations | No Siri or App Intents recording hook exists; only Apple Reminders (beta) [inferred from absence] |
| The 29 h jazz record was continuous capture | 3-hour cap (Finding 1) | Refuted [verified] |

**What started the session at 16:05 remains unknown.** It is not answerable
from outside the device; the answer is in Fieldy's backend.

## Finding 4 — three more documentation contradictions [verified]

1. **Automatic recording — the docs contradict each other outright.** The help
   center states that by default the device begins recording automatically.
   The Fieldy 3 device guide states there is no automatic recording feature
   and that recording starts only when initiated in the app. These cannot both
   be true, and they disagree on **the single question most relevant to
   consent**: whether the device can start listening on its own.
2. **Button behaviour.** Marketing copy says you press the button once to
   start capturing; the device guide says a single click is a connection-status
   check. **The device matches the guide** [verified by the researcher's
   long-standing use] — so the marketing copy is wrong.
3. **The LED indicator help article is a dead 404.** The canonical reference
   for what the light means is unavailable.

Add to the pre-existing power-hold drift (2 s vs 3 s in their own docs): in
practice a 2-second hold does **not** power the device off for this unit. A
10-second hold is documented as a power reset; untested at time of writing.

## Finding 5 — the LED question is open, and its obvious confound is eliminated

**Control [verified]:** at 21:23 local the researcher ran an 11-second
button-started recording in the *same* record-only mode (quota exhausted).
The LED lit on activation and went out on stop. **Record-only mode does light
the LED.** This killed the first hypothesis — that quota-exhausted capture is
silently unindicated.

**A confound was proposed and then eliminated.** The analyst suggested the
21:23 control might not represent a 16:05–18:20 event, because afternoon
daylight could mask a small LED that reads clearly at night. **The researcher
reports the room's light level does not vary meaningfully by time of day.**
The control is therefore valid for the event window.

**So the situation is:** for 2 h 15 m the researcher sat within peripheral view
of the pendant, under lighting equivalent to a control in which the LED was
plainly noticeable, and **observed no lit LED** — while a recording was
demonstrably running.

Two readings survive, and this study cannot distinguish them:

- **(a)** The LED was lit and went unnoticed across two hours of absorbed desk
  work, despite being obvious in a deliberate 11-second test. Attention in a
  test is not attention while working; habituation to a familiar object in
  peripheral vision is real.
- **(b)** A session that starts *without user action* does not light the LED
  the way a button-started session does.

**(b) would be a serious defect** — capture with no signal to the wearer or to
anyone nearby. It is recorded as open, not concluded. Resolving it requires
observing a spontaneous start, which cannot be scheduled.

## What this means for RQ5 (consent)

Independent of which reading is right, the event itself is the finding:
**a three-hour recording of a private home ran without its owner's knowledge,
and he discovered it only by reading a billing screen.** Bystanders had no
opportunity to consent to something the wearer did not know was happening.

## The question for the vendor

Precise, answerable server-side, and useful to them:

> Conversation `aa139733-a3e3-5f15-95ea-d7b098cccdc4` began at
> 2026-07-20T22:05:21.747Z and ran to the 3-hour cap. The user initiated
> nothing. **What started this session?** And does a session that starts
> without user action drive the LED indicator?

## Method note — this analysis was wrong four times before it was right

Recorded because the study's rules require it, and because the pattern is
instructive. In the course of this single investigation the analyst:

1. Claimed a 29-hour session consumed ~1,764 minutes — **wrong**, it was ~62
   minutes of audio (notebook 015).
2. Concluded "reporting artifact" with unwarranted confidence, on reasoning
   that did not exclude the alternative — **overstated**.
3. Inferred from a `locationId` that the phone was the capture source —
   **invalid**; pendant-recorded conversations carry `locationId` too.
4. Proposed phone-microphone capture as the mechanism — **the feature does not
   exist**.
5. Proposed daylight as the reason the LED went unseen — **eliminated**; the
   room's lighting is constant.

**Every one was corrected by the researcher's direct physical observation, not
by better analysis.** The generalisable lesson, now demonstrated repeatedly:
**Fieldy's own metadata is an unreliable substrate for inference. Physical
observation outranks it every time.** Where the two conflict, the metadata is
what should be doubted first.
