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
4. **"Preamble, scooter, under the shirt"** (riding): jumbled. **Corrected
   attribution (researcher firsthand):** the pendant was bouncing and the
   shirt rippling heavily during the ride — so this degradation is real
   mechanical + wind noise, NOT just recitation error as first written.
   This is the one take where the acoustic conditions visibly beat the
   pipeline.
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

## Caveat — clean transcript =/= clean audio (don't overstate wind-robustness)

The coherent output does NOT prove the mic captured clean sound. Fieldy's
ASR (ElevenLabs) uses a strong language-model prior and predicts likely
words — and **the Preamble is maximally predictable text**, so it can be
reconstructed from badly degraded audio by the prior alone. Combined with
the researcher's own account (wind was mild — "slightly windy," "a light
breeze"), the honest claim is **"coherent output in mild wind on highly
predictable text,"** NOT "wind-proof."

Supporting evidence that the audio *was* being stressed: take 4
(scooter, under shirt) degraded audibly, and the researcher confirms the
pendant was bouncing and the shirt rippling — real mechanical/wind noise
the prior could not fully rescue. So the pipeline's limit *was* reached;
predictable text just hid it elsewhere.

**Prior-proof retest (queued):** read UNPREDICTABLE content in real wind —
Script C (numbers, IPs, proper nouns like "Okonkwo", "192.168.20.111")
that a language model cannot guess from context. If those survive wind,
that's genuine robustness. Pair with the DJI reference recorder for
ground-truth audio. Deferred until it is cooler than 97 F outside.

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
