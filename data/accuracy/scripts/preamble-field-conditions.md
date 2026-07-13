# Preamble — field/wind/motion conditions (RQ3 extension)

Ground-truth reference for outdoor, wind, and motion takes. Text is the
US Constitution Preamble (public domain); reader has it memorized.

## Reference (52 words)

> We the People of the United States, in Order to form a more perfect
> Union, establish Justice, insure domestic Tranquility, provide for the
> common defence, promote the general Welfare, and secure the Blessings
> of Liberty to ourselves and our Posterity, do ordain and establish
> this Constitution for the United States of America.

Score Fieldy output against what the reader actually said; American-spelling
variants ("defense"/"ensure") are reader variants, amended per method, not
ASR errors.

## Conditions & slates

Each take: speak the slate, pause ~a few seconds, read the Preamble, pause
before the next (so Fieldy splits them into separate conversations).

| Slate spoken | Condition | Variable under test |
|---|---|---|
| "Preamble, collar, windy" | pendant on lanyard, outdoors, wind | baseline outdoor + wind |
| "Preamble, under shirt, windy" | same spot, tucked under a thin shirt | fabric as windscreen vs. rustle |
| "Preamble, scooter" | riding a scooter | high-speed wind + road/motor noise |
| "Preamble, helmet" | pendant inside motorcycle helmet | enclosed cavity: wind-shielded, close to mouth |

## Hypotheses (to confirm/refute)

- Under-shirt reduces wind buffeting (fabric windscreen) but adds clothing
  rustle when moving — net unknown. [inferred]
- Scooter at speed is wind-dominated; expect worst WER. [inferred]
- **Helmet may be the best moving condition** — enclosed, wind-shielded,
  near the mouth — possibly beating even collar-worn in wind. [inferred,
  the interesting one to test]

Results -> `../results.csv` + notebook entry on return.
