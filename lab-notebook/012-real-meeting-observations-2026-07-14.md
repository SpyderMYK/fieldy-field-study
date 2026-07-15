# 012 — Observations from a real ~53-min multi-party meeting

**Date:** 2026-07-14. Fieldy used to capture a real multi-party video
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

3. **~~Largest timestamp error observed to date: ~1+ day.~~ RETRACTED —
   this was an analyst error, not a Fieldy bug.** Original claim: the
   meeting appeared stamped a day ahead. **Correction:** the researcher
   confirmed the meeting was on the evening of the 14th (local), which in
   UTC is the early hours of the 15th — exactly what Fieldy recorded.
   Fieldy's timestamp was **correct.** The assistant had assumed the wrong
   meeting date and pattern-matched to the known anchor-late bug
   (confirmation bias). Fieldy's only *verified* timestamp issue remains the
   ~90-s anchor-late start offset (notebook 009). Lesson: don't attribute to
   a device bug what a wrong assumption explains.

4. **UTC/local date-boundary gotcha (querier-side, not a device bug).** An
   evening-local meeting lands on the *next* UTC calendar day, so a
   `GET /conversations?startTime&endTime` window built around the local date
   can miss it by hours. That is what happened here — the REST query used
   the wrong day, and the MCP `list_recent_conversations` tool (no time
   filter) surfaced it immediately. **Practical rule:** to find a recent
   conversation, prefer list-recent over a hand-built time window, and if
   using a window, remember Fieldy timestamps are UTC.

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
