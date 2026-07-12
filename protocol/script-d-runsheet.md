# Script D run sheet — two-speaker take (~5 minutes total)

What this measures: speaker labeling with a real second person (RQ3/RQ5 —
does the wearer get a distinct label? what does the second speaker get?)
and Fieldy's automatic task extraction, scored against the script's
six-commitment table (recall/precision).

## Before the take

1. Consent: the second speaker agrees to be recorded and knows the study
   publishes transcripts. Note: script D is *scripted* dialogue — the words
   are already public in this repo — so the published payload contains no
   personal content; the participant is recorded as "consenting
   participant" without name.
2. Quiet room, TV off. Pendant on the wearer, steady-white LED confirmed.
3. Both speakers can read from one screen or two copies of
   [`../data/accuracy/scripts/ground-truth-scripts.md`](../data/accuracy/scripts/ground-truth-scripts.md)
   (Script D section).

## The take

1. Wearer speaks the slate: **"R Q three, session D quiet one."**
2. Read the dialogue naturally — wearer reads Speaker 1, participant reads
   Speaker 2. Slight overlaps fine (note them afterward if they happen).
3. Wearer ends the conversation manually in the app.
4. Note the clock time at end.

## After (assistant handles)

- Pull webhook payload: speaker label assignment (wearer vs. participant).
- `GET /tasks?status=new` — what did Fieldy extract? Score against the
  six-commitment table (owner, due date, recall/precision).
- Check `memoryId` linkage from extracted tasks back to the conversation.
- Results → notebook entry + `results.csv`.

## If time allows (optional +3 min)

Repeat as **D-tv-1** with the TV on at conversational volume — the
three-way case (wearer + participant + broadcast voices) is the realistic
household condition and directly extends the entry-004 finding.
