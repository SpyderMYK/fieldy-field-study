# 005 — RQ3 Script C: numbers flawless, names are the weak spot

**Date:** 2026-07-11 evening (payload 2026-07-12T00:30Z). Session C-quiet-1.
Sample: [`../data/samples/payload-003-numbers-jargon.json`](../data/samples/payload-003-numbers-jargon.json).

## Result — WER ≈ 3%, every error a proper-noun spelling

**Numeric normalization: 100%.** Every spoken number rendered correctly in
written form: date ("March 3"), time ("9:45"), currency ("$12,500",
"$19,080"), percentage ("52%"), version ("DOCSIS 3.1"), VLAN/port numbers,
and — most impressive — the spelled-out IP address rendered as a perfect
dotted quad: **192.168.20.111**.

**Proper nouns: 4 substitutions** (the take's only errors):

| Said | Transcribed | Note |
|---|---|---|
| OPNsense | "OpenSense" | phonetically faithful, lexically wrong |
| Ms. | "Mrs." | honorific swap |
| Okonkwo | "Okuoko" | the one name missed — Nguyen, Rajesh, Siobhan, Xavier all correct |
| Arris | "ARIS" | spelling/casing of same phonetics |

**Self-corrections are transcribed verbatim.** The reader stumbled on
"S thirty-three" and corrected aloud; the transcript preserved the stumble
and the correction ("—oops, that should be 33—") with no disfluency
cleanup. Downstream automations receive raw speech, not tidied speech.

Reader deviations this take (reference amended per method): "received" for
"reviewed", plus the stumble region.

## Running RQ3 tally

| Take | Condition | Wearer WER | Character |
|---|---|---|---|
| B-quiet-1 | quiet | 0 | verbatim |
| A-tv-1 | TV @3m | 0 | verbatim through interference |
| C-quiet-1 | quiet, numbers/names | ~3% | all errors proper-noun orthography |

Emerging picture: the ElevenLabs pipeline is exceptional on common English
and number normalization, and degrades only on out-of-vocabulary proper
nouns — a very usable error profile (numbers and dates in tasks/reminders
can likely be trusted; rare names cannot).

## Next in session

Webhook retry test (RQ1) → offline-storage timestamp experiment (RQ6).
