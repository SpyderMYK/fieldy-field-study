# 014 — Real two-speaker conversation in a restaurant

**Date:** 2026-07-20. Fieldy used in a real ~27-minute two-person
conversation in a restaurant (both parties consenting). **No content,
names, or topic appear here** — device behavior only. Complements the
crowded-meeting case (notebook 012) and the TV-contamination case
(notebook 004).

Shape (non-identifying): ~27 min, ~4,000 words, 2 human speakers + ambient
restaurant noise, phone present (all segments `source: live`).

## Findings

1. **Two-speaker diarization is clean [key positive].** The device split
   the conversation into two well-balanced speakers — 171 vs 180 segments,
   a near-even 50/50 — cleanly separating the two people across a long
   back-and-forth. This is the direct answer to the open question from the
   crowded meeting (notebook 012, where ~8 people collapsed into fewer
   labels): **diarization quality scales inversely with speaker count** —
   excellent at 2, degrades with a crowd. It is not "real conversation" that
   breaks it; it's the number of voices.

2. **Restaurant noise contaminated very little.** Only 3 stray segments got
   a third speaker label (a server or nearby table) out of 354 total — minimal
   phantom-speaker bleed. Contrast the TV test (notebook 004), where a
   television playing dialogue flooded the transcript with fictional
   speakers. **General ambient murmur is not the problem; intelligible
   far-field speech (a TV, a nearby distinct conversation) is.** A noisy room
   of unintelligible crowd noise is handled far better than one clear
   competing voice source.

3. **Still no distinct wearer designation** — the wearer is just "Speaker 1,"
   not specially marked (consistent with every prior take).

4. **Timestamp correct here** — the conversation was stamped at the actual
   local lunch time (verified against the researcher's own clock). So the
   anchor-late offset (notebook 009) isn't visible at this granularity, and
   there is no coarse date error on this take. (Reinforces: don't assume a
   timestamp bug — check the real time first.)

5. Many short fragments (102 segments of <=2 words) — normal for a lively
   two-way exchange, not a defect.

## Assessment

The most favorable real-world take so far: clean 2-speaker separation and
low noise contamination. Combined with 004 and 012, the diarization picture
is now: **great at 2 speakers, poor at ~8; broadcast/again-intelligible
speech is the contaminant, not room noise.** A useful, nuanced result for
the "lunch with a friend" use case Fieldy markets.
