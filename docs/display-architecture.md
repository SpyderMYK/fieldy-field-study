# Flexible multi-display architecture

Goal: one content pipeline, many display nodes — each rendering in its
native strengths. Add or remove a screen without touching the brain.

## The bus

The "brain" (roast or Q&A) does not talk to any screen directly. It
publishes a message to a **bus file on alien**, served by the signage
HTTP server (`:8088`). Every display node polls the bus and renders what
it can. This is why the system is flexible: the brain has one job
(produce a message), displays have one job (render the current message).

**Bus file:** `/opt/signage/heckler.json` (served at
`http://alien:8088/heckler.json`). Plain-text projection
`heckler.txt` is kept for the current LED node (backward compatible).

**Schema:**

```json
{
  "ts": 1752... ,          // publish time (epoch seconds)
  "mode": "qa|roast|idle", // what produced it
  "line1": "…",            // short line 1
  "line2": "…",            // short line 2
  "short": "line1 line2",  // one-line form (LED scroller)
  "full":  "…"             // longer body (e-paper / HDMI layouts)
}
```

Displays consume only the fields they can use. As the brain grows richer
output (a paragraph answer, a title, an image), new fields are added;
old displays ignore them.

## Display nodes (each subscribes to the same bus)

| Node | Renders | Strength | Status |
|---|---|---|---|
| **LED matrix** (MatrixPortal M4 + HUB75) | `short` / `line1`+`line2`, scrolling | bright, room-readable, motion; readable in the dark | **built** |
| **E-paper** (7.5" 800×480, bare + driver) | `full` as a static high-res page | ultra-low power, daylight-readable, sharp; NO motion, needs ambient light | planned |
| **HDMI screen** (UNO Q → monitor/TV) | full color layout or "training video" | high res, full color, video/motion | planned (UNO Q en route) |

Each is independent: run one, run all three, run none. Same words appear
on every connected screen, formatted to its medium — LED scrolls the
one-liner, e-paper prints the full answer as a crisp page, the HDMI
screen does the full-color gag.

## Why this shape

- The brain never needs to know what screens exist.
- A screen can join mid-show (poll starts, picks up current message).
- Failure isolation: a wedged display node can't take down the pipeline
  (already true — see the LED brownout episode; the brain kept running).
- New medium = new small poll-and-render script, nothing else changes.

## Build order

1. Bus published by both brains (done — text projection retained).
2. LED node: optionally switch from `heckler.txt` to `heckler.json`
   (`short` field) — cosmetic, not required.
3. HDMI node when the UNO Q arrives: a fullscreen browser/kiosk on the
   UNO Q polling the bus (richest, closest to the original comedy vision).
4. E-paper node last: verify the exact bare-panel + driver-board pairing
   before ordering; then a static-page renderer for `full`.

### E-paper — open compatibility question (parked, still wanted)

Researcher wants the e-paper node; blocked on a verified driver+panel
pair. Finding (2026-07-13): the Adafruit RP2040 Feather ThinkInk (#5727,
all-in-one RP2040 + 24-pin FPC socket) is **only tested up to 5.6"** per
Adafruit docs — 7.5" 800x480 UC8179 support is unconfirmed. The board's
"optional" add-ons (STEMMA QT cables, stacking headers) are irrelevant to
this use. Before ordering, resolve ONE of:
- a panel size the ThinkInk definitely drives (<=5.6"), OR
- confirm #5727 drives the 7.5" UC8179 (Adafruit support / library), OR
- a different controller for the full 7.5" (Waveshare 7.5" + its driver
  HAT on a Pi, or drive it from the UNO Q Linux side).

### Power parts ordered 2026-07-13 (Adafruit #2697 + #368)

For running the built LED node off the Anker PowerCore 20100 — see
`src/heckler_panel/README.md` for the wiring.
