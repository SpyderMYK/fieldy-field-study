# 009 — Live-polling experiment: no mid-conversation transcripts; anchor-late confirmed

**Date:** 2026-07-12 morning. One take, two questions answered.

## Design

API polled every 12 s (26 polls, well under rate limit) across a ~3-minute
open conversation. Researcher spoke a **time hack immediately after
pressing Start** ("I pressed the start clock at exactly [time]"), giving a
true anchor reference with ~1 s uncertainty. (Researcher initially spoke
the wrong hour — wrong clock — corrected on review; minutes/seconds were
consistent throughout.)

## Result 1 — transcripts reach the server only at conversation end [verified]

**Zero segments visible through the entire open conversation; all 5
appeared in one burst after manual end.** Fieldy's cloud has no
mid-conversation transcript access — the phone app's live view is
phone-local. Any real-time integration built on the webhook or API is
structurally impossible; the minimum unit of latency is the conversation.

Measured end-of-conversation pipeline: manual end → webhook ≈ **seconds**;
end → API-visible ≤ ~16 s.

## Result 2 — anchor-late hypothesis CONFIRMED [verified]

True press-to-speech: time hack spoken at start-offset 1.0 s, true time
17:26:45 UTC. Claimed segment timestamp: 17:28:20 — the conversation
anchor was stamped **94 s after true start**, within the ~60–112 s band
seen in every take since first light. Offsets are honest; the anchor is
systematically late; all absolute speech times inherit ~1.5 min of error.
Theory v2 (entry 007) is now measured fact; the offsets-inflated
alternative is dead.

## Why this take existed — the performance-rig concept

A proposed public-facing build (UNO Q display node + Fieldy + local LLM):
a live routine where the wearer talks about AI while a screen behind them
— which they can't see — shows an AI's commentary on what they're saying.
Comedy mode (straight man / AI comic) and public-education mode (showing
an audience in real time what a wearable captures and infers — RQ5's
findings as an exhibit).

Feasibility verdict from today's numbers: live heckling is impossible
(Result 1), but a **beat-delayed format works**: end-of-bit tap → roast on
screen in ~10–15 s (webhook seconds + local LLM ~3–5 s + render). The
constraint becomes the format: the screen "catches up" between bits.

## Next for the rig

- UNO Q arrives: display-node prototype (fullscreen renderer fed from
  alien; MCU side free for stage props).
- Heckler prompt engineering on oracle (persona, brevity, safety rails).
- Audience-recording ethics: announce-at-start rule; audience transcripts
  never published (protocol already covers).
