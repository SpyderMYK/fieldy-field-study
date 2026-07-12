# Heckler panel

Display node for the performance rig (notebook 009): an Adafruit
MatrixPortal M4 driving a P6 64x32 HUB75 RGB matrix, scrolling short
messages produced by the local pipeline (Fieldy webhook -> alien ->
local LLM on the homelab -> panel).

Status: hello-world scroller verified (clean scroll, stage-bright,
stable on a Mac USB-C port at moderate color values; full-brightness
stage use wants a separate 5V 4A supply per Adafruit's power guide).

- `code.py` — current CircuitPython program (CP 7.1.0-compatible,
  no-network scroller). Wi-Fi + HTTP polling of the roast endpoint is
  the next stage.
- Wearer-visible disclosure and audience announcement rules for any
  public use are in the study protocol (Recording rules).
