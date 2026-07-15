# 012 — Observations from a real ~53-min multi-party meeting

**Date:** 2026-07-13. Fieldy used to capture a real multi-party video
meeting (Zoom, one in-room wearer + remote participants). **No meeting
content, names, or specifics appear here or anywhere in this repo** — the
transcript and derived minutes are private. Only device/pipeline behavior
is recorded below.

Shape (non-identifying): ~53 min, ~7,000 words, ~8 human participants.

## Findings

1. **The AI summary covers only the opening ~10 minutes of a 53-min
   meeting.** Fieldy's auto-summary described the first few agenda items and
   silently omitted the entire back two-thirds — including the meeting's
   most consequential discussion. **Major limitation for long
   conversations:** the summary reads as complete but drops most of the
   content. For any minutes/recap use, the summary is not trustworthy on
   its own; the full transcript must be processed. (Reinforces notebook
   008: a local model given the full transcript produced complete minutes;
   Fieldy's own summarizer did not.)

2. **Diarization merges distinct speakers.** Several different remote
   participants were collapsed into a single "Speaker" label, and the
   wearer was mislabeled with a different person's name once. Audio-only
   diarization loses who-said-what that a video roster gives at a glance —
   the two channels are complementary, and audio alone is insufficient for
   attributed minutes. (n: 6 speaker labels emitted for ~8 people.)

3. **Largest timestamp error observed to date: ~1+ day.** The meeting was
   stamped ~24-plus hours ahead of real time (a same-evening meeting
   appeared dated two calendar days later in UTC). This dwarfs the ~90-s
   anchor-late offset characterized in notebook 009 and suggests a separate,
   coarser failure (device/app clock or offline-sync date assignment), not
   just the fine anchor lag.

4. **The timestamp error breaks time-window queries.** Because the record's
   startTime was mis-stamped, `GET /conversations?startTime&endTime` over
   the real meeting window returned nothing — the meeting fell outside the
   queried range. The MCP `list_recent_conversations` tool (no time filter)
   surfaced it immediately. **Practical rule:** do not rely on time-range
   queries to find a conversation; Fieldy's own timestamps can place it
   outside any sane window. List-recent / cursor paging is more reliable.

5. **Transcript paging quirk.** `GET /transcriptions` capped at 50 segments
   with a null `nextCursor` despite more segments existing; full retrieval
   required manually advancing `startTime` past the last returned segment.
   Cursor pagination is unreliable on this endpoint.

6. **Proper-noun mangling at real-world scale.** Brand names, vendor names,
   and personal names were frequently mis-rendered (consistent with
   notebook 005). In a real meeting this means names of people, companies,
   and products in the transcript cannot be trusted without correction.

## Assessment

Transcription of intelligible speech was good; everything *downstream* of
raw words — summary completeness, speaker attribution, timestamps, and
proper nouns — degraded in ways that matter for the marquee "meeting
notes / minutes" use case. A real 53-minute meeting is where Fieldy's
summarizer visibly fails, in a way short test clips never exposed.
