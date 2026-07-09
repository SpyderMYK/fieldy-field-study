# Ground-truth reading scripts

Read verbatim. The printed text below is the scoring reference — see
[README.md](README.md) for procedure and normalization rules.

---

## Script A — Rainbow Passage (standard connected speech, ~180 words)

Phonetically rich standard passage used across decades of speech research;
tests connected, flowing speech with no unusual vocabulary.

> When the sunlight strikes raindrops in the air, they act as a prism and form
> a rainbow. The rainbow is a division of white light into many beautiful
> colors. These take the shape of a long round arch, with its path high above,
> and its two ends apparently beyond the horizon. There is, according to
> legend, a boiling pot of gold at one end. People look, but no one ever finds
> it. When a man looks for something beyond his reach, his friends say he is
> looking for the pot of gold at the end of the rainbow. Throughout the
> centuries people have explained the rainbow in various ways. Some have
> accepted it as a miracle without physical explanation. To the Hebrews it was
> a token that there would be no more universal floods. The Greeks used to
> imagine that it was a sign from the gods to foretell war or heavy rain. The
> Norsemen considered the rainbow as a bridge over which the gods passed from
> earth to their home in the sky.

## Script B — Harvard sentences, set 1 (short isolated sentences)

Ten phonetically balanced sentences; tests short-utterance accuracy without
surrounding context. Pause about two seconds between sentences.

> 1. The birch canoe slid on the smooth planks.
> 2. Glue the sheet to the dark blue background.
> 3. It's easy to tell the depth of a well.
> 4. These days a chicken leg is a rare dish.
> 5. Rice is often served in round bowls.
> 6. The juice of lemons makes fine punch.
> 7. The box was thrown beside the parked truck.
> 8. The hogs were fed chopped corn and garbage.
> 9. Four hours of steady work faced us.
> 10. A large size in stockings is hard to sell.

## Script C — Numbers, names, and technical vocabulary (~130 words)

Custom passage targeting known ASR weak spots: digits, times, model numbers,
and domain jargon. **Numeral convention for scoring:** the reference for
digits is the spoken form printed in brackets — e.g. read "192.168.20.111" as
"one ninety-two dot one sixty-eight dot twenty dot one eleven".

> The meeting is on Tuesday, March third, at nine forty-five in the morning.
> Our budget rose from twelve thousand five hundred dollars to nineteen
> thousand eighty dollars, an increase of about fifty-two percent. The server
> rack holds an OPNsense firewall, a ZFS storage pool named tank, and a
> Proxmox hypervisor on VLAN twenty. Doctor Nguyen and Ms. Okonkwo reviewed
> the DOCSIS three point one modem, an Arris Surfboard S thirty-three,
> before switching the Tailscale exit node. The IP address is one ninety-two
> dot one sixty-eight dot twenty dot one eleven, and the fallback port is
> eighty-four forty-three. Email the CSV to procurement by Friday the
> twenty-first, and CC Rajesh, Siobhan, and Xavier on the follow-up.

## Script D — Two-speaker dialogue with embedded commitments (~1.5 min)

Tests speaker labeling (Fieldy marks the wearer distinctly; others get A–E)
and automatic task extraction. Speaker 1 is the wearer. Both speakers consent
to recording. Read naturally; slight overlaps are fine and should be noted in
the session log if they occur.

> **Speaker 1:** Did you get a chance to look at the garage shelving plan?
> **Speaker 2:** I did. I think the wall anchors you picked are rated too low
> for the load. We should swap them out.
> **Speaker 1:** Fair enough. I'll order the heavier anchors tonight and I'll
> send you the tracking number tomorrow.
> **Speaker 2:** Sounds good. Also, don't forget the dentist moved your
> appointment to Thursday at two thirty.
> **Speaker 1:** Right, thanks. Remind me to call the pharmacy before noon
> tomorrow about the refill.
> **Speaker 2:** Will do. And I promised Elena we'd return her ladder this
> weekend — can you put it in the truck Saturday morning?
> **Speaker 1:** Yes, I'll load the ladder Saturday morning before breakfast.
> One more thing: I need to renew the car registration by the end of the
> month, so I'll do that online Friday.
> **Speaker 2:** Perfect. Then we're set.

**Commitment table for task-extraction scoring** (what a perfect extractor
should catch):

| # | Commitment | Owner | Due |
|---|---|---|---|
| 1 | Order heavier wall anchors | wearer | tonight |
| 2 | Send tracking number | wearer | tomorrow |
| 3 | Dentist appointment (reschedule awareness) | wearer | Thursday 2:30 |
| 4 | Call pharmacy about refill | wearer | before noon tomorrow |
| 5 | Load Elena's ladder in truck | wearer | Saturday morning |
| 6 | Renew car registration online | wearer | Friday / end of month |

## Script E — Spontaneous speech (unscripted protocol)

No printed text. For naturalistic sessions, ground truth is the reference
recording transcribed with whisper.cpp large-v3 and then **hand-corrected by
the researcher against the audio**. Only self-recorded or consenting-speaker
audio is used; the corrected transcript, not the audio, may be published if
it contains no third-party content.
