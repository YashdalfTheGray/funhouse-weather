import board
import time
import adafruit_dps310
import adafruit_ahtx0

from secrets import secrets
from adafruit_funhouse import FunHouse

# some global labbels/state that will exist
value_label = None
unit_label = None

# set up the sensors
i2c = board.I2C()
dps310 = adafruit_dps310.DPS310(i2c)
aht20 = adafruit_ahtx0.AHTx0(i2c)

# setup the funhouse controller
funhouse = FunHouse(default_bg=0x000000)

# clear the display and lights, and then show the splash screen
funhouse.display.show(None)
funhouse.peripherals.set_dotstars(
    0x000000, 0x000000, 0x000000, 0x000000, 0x000000)
funhouse.display.show(funhouse.splash)

# setup some labels for the screen
value_label = funhouse.add_text(
    text=f"{dps310.temperature:.1f}",
    text_position=(120, 120),
    text_scale=6,
    text_color=0xFFFFFF,
    text_anchor_point=(0.5, 0.5)
)

while True:
    funhouse.set_text(f"{dps310.temperature:.1f}", value_label)
    time.sleep(0.5)
