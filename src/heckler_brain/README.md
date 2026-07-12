# Heckler brain

Fieldy transcript -> local LLM roast -> LED panel feed. The last stage of
the performance rig (notebook 009).

Pipeline: watches the Fieldy webhook archive on alien; on each new
speech-bearing conversation, sends the transcript to the local model
(qwen2.5:14b-instruct via Ollama on oracle) with a deadpan-heckler prompt,
and writes two <=40-char all-caps roast lines to the panel's feed file.

Runs on herman (only host with SSH reach to both alien and oracle).

## Show-mode gate

Roasts ONLY while `~/.heckler_show_on` exists. Absent the flag the pipeline
is silent, so ambient household/lab conversation is never editorialized.
Enable with `touch ~/.heckler_show_on`; silence with `rm` of the same.

## Ethics

Public use requires the audience announcement in the study protocol
(Recording rules); audience transcripts are never published.

First verified roast (canned transcript, 2026-07-12):
"AI CHANGED EVERYTHING YEARS AGO" / "DEEP THINKER ALERT: DEEP WATER".
