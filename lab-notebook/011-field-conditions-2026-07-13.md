# 011 — Field conditions: wind, scooter, helmet (Preamble)

**Date:** 2026-07-13. RQ3 outdoor/motion extension.
Reference & plan: [`../data/accuracy/scripts/preamble-field-conditions.md`](../data/accuracy/scripts/preamble-field-conditions.md).

## Setup

~24-minute continuous outdoor session (walk + scooter), phone in pocket,
app backgrounded. Researcher recited the US Constitution Preamble
(memorized, public domain) under six placement/condition variants, ending
by pressing the device button; synced on return. Personal/ambient
commentary captured during the walk is **redacted** here per publication
rules — only the recitation takes and experiment-relevant notes are shown.

**It all transcribed.** The backgrounded-app worry was unfounded: the full
session synced and transcribed on return. Segments labeled "Speaker 1"
(not the offline "Unknown" of notebook 007), suggesting the app stayed
live-connected in the pocket.

## The takes (as transcribed by Fieldy)

1. **"Preamble, outside of shirt, not windy"** (lanyard/walk): "…secure the
   blessings of liberty to all. The United States of America." — reader
   truncated ("I may have skipped a line or two"); coherent.
2. **"Preamble, outside shirt, slightly windy"** (walk): full recitation,
   coherent, minor "do to ourselves" artifact.
3. **"Preamble, inside the shirt, fairly windy"** (light breeze, walk):
   full and clean; reader: "I think I got the whole thing right that time."
4. **"Preamble, scooter, under the shirt"** (riding): jumbled —
   "…do not forget to provide for the blessings of liberty…" — reads as the
   reader's recitation scrambling while riding, not mic failure; words
   still intelligible.
5. **"Preamble, on scooter, inside helmet"** (riding): **full, clean,
   complete** Preamble.
6. **"Preamble, inside helmet, low speed, on scooter"** (riding): **full,
   clean, complete** — pendant mounted mid-forehead inside helmet.

## Findings

- **No wind-destroyed garbling in ANY condition**, including scooter at
  speed. Refutes the pre-registered "scooter will be wind-dominated /
  worst WER" hypothesis — the near-field mic held up far better than
  predicted.
- **Helmet hypothesis CONFIRMED.** The two in-helmet takes (5, 6) were the
  cleanest and most complete of the set. The enclosed, wind-shielded,
  close-to-mouth cavity is the best moving-condition placement — exactly
  the pre-registered prediction.
- **Under-shirt vs. outside-shirt**: both intelligible on the walk; no
  dramatic difference at walking wind levels. The fabric-windscreen-vs-
  rustle tradeoff didn't clearly favor either at these speeds.
- Ergonomics note (researcher): forehead mount inside helmet is effective
  but uncomfortable; a better in-helmet mount would be needed for real use.

## Limitation — no clean WER this round

These takes CANNOT be scored for word-error-rate like the indoor takes.
The reference was recited from memory and varied take-to-take (reader's own
skips/reorderings), and there was no independent reference recording — so
Fieldy's transcript is the only record of what was said. Result is
**qualitative** (intelligible vs. garbled), not a WER.

This is the strongest case yet for the **DJI-mic reference recorder**
(scoped in `data/accuracy/scripts/README.md`): a wind-tolerant lav
recording a ground-truth track would let field takes be scored, not just
described.

## Incidental

- Researcher narrated the end time ("2:43 in Denver"); the conversation's
  API end time (20:44 UTC = 14:44 MDT) matches within ~1 minute — a rare
  accurate timestamp, likely because the button-press end anchored close
  to real time (contrast the ~94 s-late *start* anchor, notebook 009).
- Fieldy's AI titled the session "Testing Audio Recitations in Extreme
  Heat" — the summarizer latched onto the researcher's heat commentary over
  the actual recitation content; minor note on summary salience.

## Next

- DJI-mic reference recorder would upgrade field takes from qualitative to
  scored. Parked with the accuracy-rig scoping.
- Better in-helmet mount if helmet placement is pursued.
