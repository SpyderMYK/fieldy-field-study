# Heckler panel - hello world scroller (no network)
# Prior moon-clock code is backed up in LabDocs/matrixportal-backup-2026-07-12
import time
import displayio
import terminalio
from adafruit_matrixportal.matrix import Matrix
from adafruit_display_text.label import Label

MESSAGE = "HE CAN'T SEE THIS SCREEN      "
COLOR = 0xCC2200  # moderate amber-red, easy on USB power budget

matrix = Matrix(width=64, height=32, bit_depth=4)
display = matrix.display

group = displayio.Group()
label = Label(terminalio.FONT, text=MESSAGE, color=COLOR, scale=2)
label.x = display.width
label.y = 15
group.append(label)
display.show(group)

text_width = label.bounding_box[2] * 2  # account for scale
while True:
    label.x -= 1
    if label.x < -text_width:
        label.x = display.width
    time.sleep(0.03)
