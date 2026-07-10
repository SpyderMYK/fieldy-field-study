# Privacy context: AI notetakers in the mainstream press — 2026-07-10

AP News, 2026-07-09: ["AI notetakers promise easy meeting recaps, but some
professionals question their use"](https://apnews.com/article/ai-notetaker-work-meetings-privacy-data-c700299371ca7cfec77dafdfb948067f)
([syndicated copy](http://www.bozemandailychronicle.com/ap_news/business/ai-notetakers-promise-easy-meeting-recaps-but-some-professionals-question-their-use/article_441baed9-2353-5efd-94c8-c2ee98e738d3.html)).
Meeting-notetaker focused rather than wearable-focused, but most of it maps
directly onto always-on wearables — often more strongly, since a wearable
records people who never saw a meeting invite.

## What it adds to this study

1. **Voiceprints are biometric identifiers.** Privacy advocates quoted (EFF's
   Thorin Klosowski; attorneys at Baker Donelson, Fisher Phillips, The Dillon
   Law Group) warn that notetaker vendors may build voiceprints — biometric
   profiles of a voice — without consent. Illinois's BIPA requires **written
   notice, informed consent, and a documented destruction policy** before
   voiceprint collection. Directly relevant here: Fieldy's **speaker
   profiles** feature (wearer marked distinctly, others labeled A–E) is
   speaker identification — whether it constitutes voiceprint creation, and
   what Fieldy's policy says about biometric consent/retention, is now an
   explicit RQ5 sub-question. **[verified 2026-07-10]**: Colorado (this
   study's location) amended its Privacy Act via
   [HB 24-1130](https://leg.colorado.gov/bills/hb24-1130), effective
   2025-07-01 — see the Colorado-law section below.
2. **Sharing with an AI can pierce privilege.** A February 2026 New York
   federal ruling ordered a defendant to hand prosecutors documents he had
   shared with an AI assistant — third-party AI sharing can eliminate
   confidentiality protections. For a wearable: sensitive conversations
   transiting ElevenLabs/OpenAI may lose legal protections their
   participants assume they have.
3. **Retention/training/resale.** The article reiterates unknowns we already
   track (where data lives, how long, whether it trains models) and adds
   that some vendors *resell* notetaker data. Fieldy's stance on training
   and resale is vendor-self-declared only — same bucket as their
   HIPAA/E2E claims.
4. **Practical etiquette that transfers to wearables:** announce recording
   at the start, ask for consent explicitly, know the retention schedule
   before recording others. Already in our ethics rules; the article
   strengthens the case that this is mainstream expectation, not paranoia.

## Colorado law — verified against statutes and legal analyses, 2026-07-10

Not legal advice; a research record of what the sources say.

### Biometrics — CPA amendment (HB 24-1130, effective 2025-07-01)

- [HB 24-1130](https://leg.colorado.gov/bills/hb24-1130) amended the Colorado
  Privacy Act to cover **any controller processing biometric identifiers of
  Colorado residents, regardless of the CPA's usual volume thresholds**
  (analyses: [Venable](https://www.venable.com/insights/publications/2024/06/colorado-amends-state-privacy-law-to-include),
  [Littler](https://www.littler.com/news-analysis/asap/implications-employers-colorados-new-biometrics-law),
  [Hunton](https://www.hunton.com/privacy-and-information-security-law/new-colorado-law-imposes-heightened-requirements-for-the-collection-and-processing-of-biometric-data)).
- Requirements on controllers: specific **notice and consent before
  collecting/processing** biometric identifiers; a **written policy with a
  retention schedule and deletion deadlines**; a security-incident protocol;
  **no sale/lease/trade or third-party disclosure without consent**.
- Enforcement: Colorado AG and district attorneys only — **no private right
  of action** (unlike Illinois BIPA).
- **Application to this study:** the obligations fall on *controllers* —
  i.e., **Fieldy**, if its speaker profiles constitute biometric
  identifiers of Colorado residents. This puts a sharp documentary test
  under RQ5: does Fieldy provide biometric-specific notice/consent, and does
  it publish a retention-and-deletion policy? An individual's personal,
  non-commercial recording is not what the CPA regulates, so the study
  itself is out of scope on its face **[inferred — reasoning about scope,
  not verified by counsel]**.

### Recording consent — wiretap & eavesdropping statutes

- Colorado is **one-party consent**. [C.R.S. § 18-9-303](https://www.shouselaw.com/co/defense/laws/eavesdropping/)
  (wiretap, electronic communications) and
  [C.R.S. § 18-9-304](https://colorado.public.law/statutes/crs_18-9-304)
  (eavesdropping, in-person conversations): consent of **one principal
  party** is a complete defense, so the researcher recording conversations
  **they participate in** is lawful in Colorado. Violations are class 2
  misdemeanors.
- **The always-on-wearable trap:** the one-party shield only covers
  conversations the recorder is a **party to**. A wearable left running
  while its owner is absent (device on a table, jacket on a chair) records
  conversations no participant consented to — that is the exact conduct
  § 18-9-304 targets. Study rule: the device is powered off or physically
  with the researcher at all times; never left recording unattended.
- **Cross-border caveat:** calls/meetings with participants in all-party
  consent states (~11 states, e.g. California) can subject the recording to
  the stricter state's law. For any remote-meeting capture, treat the
  strictest participant state as controlling.

## Study impact

- RQ5 method expanded (protocol v1.1): check whether speaker profiles are
  described as voiceprints/biometrics anywhere in Fieldy's docs/policy;
  look for any consent, notice, retention, or destruction language tied to
  *non-wearer* voices.
- The assistive-use-case caveats in the background report get a mainstream
  citation: consent concerns around recording third parties are now
  front-page AP material, not a niche worry.
