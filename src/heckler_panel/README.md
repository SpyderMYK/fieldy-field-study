# Heckler panel

Display node for the performance rig (notebook 009/010): an Adafruit
MatrixPortal M4 driving a P6 64x32 HUB75 RGB matrix, scrolling short
messages produced by the local pipeline (Fieldy webhook -> alien ->
local LLM on the homelab -> panel).

Status: full pipeline verified end-to-end (roast + Q&A modes). Panel
joins Wi-Fi (SSID AE2N+), polls a feed file on alien's signage server.

- `code.py` — current CircuitPython program (CP 7.1.0). Single fast
  small-font mixed-case scroller, polls the feed file off-screen so the
  scroll never stutters.
- Original moon-clock firmware backed up at
  `LabDocs/matrixportal-backup-2026-07-12`.
- Wearer-visible disclosure and audience announcement rules for any
  public use are in the study protocol (Recording rules).

## Power (important)

The panel's LED current must NOT be drawn through the Mac's USB port:
that browns out the board (resets, "Disk Not Ejected" spam) and can't
sustain brightness.

Key fact (verified, Adafruit pinouts): the MatrixPortal's +5V screw
terminals are tied DIRECTLY to USB VBUS, no isolation, and are OUTPUTS
ONLY. Never inject external power into those terminals while USB is
connected -- two sources on one rail can backfeed and damage the board /
the host USB port.

### Correct external-power wiring

1. Unscrew the panel's red/black power leads from the MatrixPortal's
   screw terminals (off the board entirely).
2. Feed those leads from an external 5V supply DIRECTLY (red -> +5V,
   black -> GND).
3. Keep USB-C into the MatrixPortal for data + logic only.
4. Result: USB powers just the board; external 5V powers just the
   matrix; the two rails share only ground via the HUB75 ribbon. Safe.

### Parts to connect a USB power bank (Anker PowerCore 20100, USB-A,
### 5V/2.4A per port) to the panel leads

- Adafruit #2697 -- USB to 2.1mm Male Barrel Jack Cable, 22AWG
  https://www.adafruit.com/product/2697
- Adafruit #368  -- Female DC Power adapter, 2.1mm jack to screw
  terminal block  https://www.adafruit.com/product/368

Chain: Anker USB-A -> #2697 -> #368 -> panel red(+)/black(-). Cable is
center-positive; #368 block is marked + / -. 2.4A is ample for scrolling
text at capped brightness; a dedicated 5V/4A supply is only needed for
full-brightness dense graphics.
