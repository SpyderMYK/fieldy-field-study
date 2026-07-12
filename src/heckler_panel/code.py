# Heckler panel - stage 3: two independent scrolling lines, small font
# Feed format: heckler.txt line 1 -> top row, line 2 -> bottom row
# Backup of original moon clock: LabDocs/matrixportal-backup-2026-07-12
import time
import board
import displayio
import terminalio
from adafruit_matrixportal.matrix import Matrix
from adafruit_matrixportal.network import Network
from adafruit_display_text.label import Label

URL = "http://192.168.20.111:8088/heckler.txt"
POLL_SECONDS = 10
TOP_COLOR = 0xCC2200     # amber-red
BOTTOM_COLOR = 0x00A0CC  # cyan-ish

matrix = Matrix(width=64, height=32, bit_depth=4)
display = matrix.display

group = displayio.Group()
top = Label(terminalio.FONT, text="WIFI...", color=TOP_COLOR)
top.x = 1
top.y = 8
bottom = Label(terminalio.FONT, text="", color=BOTTOM_COLOR)
bottom.x = 20   # stagger start so lines don't move in lockstep
bottom.y = 24
group.append(top)
group.append(bottom)
display.show(group)

network = Network(status_neopixel=board.NEOPIXEL, debug=False)

current = ""
last_poll = -999.0

def set_lines(text):
    lines = (text.split("\n") + ["", ""])[:2]
    top.text = lines[0]
    bottom.text = lines[1]
    top.x = display.width
    bottom.x = display.width + 24

def width_of(label):
    return label.bounding_box[2]

while True:
    top.x -= 1
    if top.x < -width_of(top):
        top.x = display.width
        # top line off-screen: safe moment to poll
        if time.monotonic() - last_poll > POLL_SECONDS:
            last_poll = time.monotonic()
            try:
                resp = network.fetch(URL)
                new = resp.text.strip()
                resp.close()
                if new and new != current:
                    current = new
                    set_lines(current)
            except Exception as e:
                print("fetch failed:", repr(e))
    bottom.x -= 1
    if bottom.x < -width_of(bottom):
        bottom.x = display.width
    time.sleep(0.03)
