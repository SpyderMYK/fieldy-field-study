# Heckler panel - stage 2b: poll alien; fetch only while text is off-screen
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
COLOR = 0xCC2200

matrix = Matrix(width=64, height=32, bit_depth=4)
display = matrix.display

group = displayio.Group()
label = Label(terminalio.FONT, text="WIFI...", color=COLOR, scale=2)
label.x = 1
label.y = 15
group.append(label)
display.show(group)

network = Network(status_neopixel=board.NEOPIXEL, debug=False)

message = ""
last_poll = -999.0

def show(text):
    label.text = text
    label.x = display.width

while True:
    label.x -= 1
    if label.x < -(label.bounding_box[2] * 2):
        label.x = display.width
        # text fully off-screen: network pause is invisible here
        if time.monotonic() - last_poll > POLL_SECONDS:
            last_poll = time.monotonic()
            try:
                resp = network.fetch(URL)
                new = resp.text.strip()
                resp.close()
                if new and new != message:
                    message = new
                    show(message)
            except Exception as e:
                print("fetch failed:", repr(e))
    time.sleep(0.03)
