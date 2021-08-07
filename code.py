# commit3
# changed a lot about how the text is rendered on screen

import ssl
import wifi
import socketpool
import adafruit_requests
import time

from secrets import secrets
from adafruit_funhouse import FunHouse

# some functions to help set everything up


def get_current_time(requests):
    TIME_URL = f"https://io.adafruit.com/api/v2/{aio_username}/integrations/time/strftime?x-aio-key={aio_key}"
    TIME_URL += "&fmt=%25A|%25b%20%25e%2C%20%25Y|%25I%3A%25M%20%25p%20%25Z"

    response = requests.get(TIME_URL)
    return response.text.split("|")


def get_default_text_style():
    return {
        "text_color": 0xFFFFFF,
        "text_anchor_point": (0, 0),
        "text_scale": 3,
    }


# setup the funhouse controller
funhouse = FunHouse(default_bg=0x000000)

# clear the display
funhouse.display.show(None)

# get our username, key and desired timezone
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]
location = secrets.get("timezone", None)

# enable and connect to the wifis
wifi.radio.stop_scanning_networks()
wifi.radio.connect(secrets["ssid"], secrets["password"])
# print("Connected to %s!" % secrets["ssid"])
# print("My IP address is", wifi.radio.ipv4_address)

# create a request pool and something to send requests with
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

current_day, current_date, current_time = get_current_time(requests)

day_label = funhouse.add_text(
    text=current_day, text_position=(5, 0), **get_default_text_style()
)
date_label = funhouse.add_text(
    text=current_date, text_position=(5, 50), **get_default_text_style()
)
time_label = funhouse.add_text(
    text=current_time, text_position=(5, 100), **get_default_text_style()
)
funhouse.display.show(funhouse.splash)


while True:
    time.sleep(5)
    current_day, current_date, current_time = get_current_time(requests)
    funhouse.set_text(current_day, day_label)
    funhouse.set_text(current_date, date_label)
    funhouse.set_text(current_time, time_label)
