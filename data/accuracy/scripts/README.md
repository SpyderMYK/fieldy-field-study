# RQ3 ground-truth method

How transcription-accuracy sessions are run and scored. The passages the
researcher reads are in [ground-truth-scripts.md](ground-truth-scripts.md).

## Principle

Ground truth is **the text as printed here**, read aloud verbatim. Where a
passage is based on a classic ASR test text (Rainbow Passage, Harvard
sentences), fidelity to the historical original doesn't matter — what matters
is that the reader reads exactly what this file says, so word error rate (WER)
is computed against a known reference.

## Session procedure

1. Pick a script (A–D) and a condition (see matrix below).
2. **Start a reference recording** on a second device placed at similar
   distance to the Fieldy device. This is the control: the same audio
   transcribed locally with whisper.cpp large-v3 gives an on-prem ASR
   baseline to compare Fieldy's cloud pipeline against. See "Reference rig"
   below for hardware options.
3. Speak the session slate first: "R Q three, session `<script letter>`
   `<condition>` `<take number>`" — this appears in both transcripts and
   aligns Fieldy events with reference recordings.
4. Read the script at a natural pace. Do not correct mistakes mid-read; note
   any deviation from the printed text in the session log afterward (deviations
   amend the reference text for that take).
5. Log: date/time, script, condition, take, device placement, battery level.

## Condition matrix (per protocol RQ3)

| Code | Condition |
|---|---|
| `quiet` | quiet room, no background media |
| `tv` | television playing speech content at conversational volume ~3 m away |
| `duo` | two-speaker dialogue (script D), both consenting |
| `out` | outdoors, street-adjacent |

Minimum 2 takes per script × condition cell that applies (scripts A–C: quiet,
tv, out; script D: quiet, tv).

## Reference rig

Requirement for scored takes: matched placement (reference mic clipped
adjacent to the Fieldy device on the chest) so both instruments hear the
same signal. An iPhone's built-in mic is acceptable for `quiet` takes;
`tv`/`out` takes and placement parity want a wireless lav.

Hardware landscape, verified 2026-07-09 — the qualifying spec is
**standalone onboard recording on the transmitter**, so ground truth doesn't
depend on a radio link:

| System | Onboard TX recording | Notes |
|---|---|---|
| DJI Mic 3 | ✔ 32-bit float, 32 GB, dual-file (original + enhanced), timecode | Preferred: score the *original* track (reviews criticize the enhanced processing); timecode replaces the spoken slate for alignment |
| DJI Mic 2 | ✔ 32-bit float, 8 GB, ~11 h | Fully adequate |
| DJI Mic Mini 2S | ✔ 32-bit float, 14.5 GB | Launched China 2026-07-02; availability TBD |
| DJI Mic Mini | ✘ (no internal storage) | Disqualified as reference recorder |
| Rode Wireless Micro | ✘ (records via receiver/phone only) | Disqualified as standalone; fine as phone input |
| Rode Wireless GO II | ✔ 24-bit/48 kHz, ~7 h uncompressed | Adequate; fixed 24-bit, shorter runtime |

Caveat **[verified, DJI Mic 2 FAQ]**: DJI transmitters disable internal
recording while Bluetooth-connected to a phone — run standalone (or via the
receiver) for scored takes.

A transmitter with onboard recording also enables a possible third study arm:
a fully local pipeline (TX records all day → whisper.cpp batch transcription
on-prem, audio never leaves the network) compared against Fieldy's cloud on
identical days. Not scheduled; recorded here as a design option.

## Open question (moved to Day 1 checklist)

Does the Fieldy **phone app** record from the phone's microphone / active
audio input (vs. only syncing from the wearable)? If yes, iPhone + lav
becomes a way to feed higher-quality audio through Fieldy's cloud pipeline —
separating microphone hardware from cloud-pipeline quality on Fieldy itself.

## Scoring

- WER computed per take with a standard normalization: lowercase, strip
  punctuation, numerals spelled per the convention printed in each script.
- Scoring script to live in `src/analysis/` (Python, `jiwer`).
- Score three transcripts per take where available: (1) Fieldy app transcript,
  (2) webhook payload transcript (they may differ — that's a finding), and
  (3) whisper.cpp large-v3 on the reference audio.
- For script D, additionally record speaker-attribution errors (words assigned
  to the wrong speaker) and whether TV speech is falsely attributed to a
  human speaker.
- Fieldy's auto-extracted tasks from script D are checked against the
  commitments table printed with the script (task-extraction recall/precision).

## Results

Per-take results accumulate in `../results.csv` (created with first data);
analysis write-ups in `../` as they land.
