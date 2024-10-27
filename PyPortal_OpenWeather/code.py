# SPDX-FileCopyrightText: 2019 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# 

# mod by Rich Whiffen - 12/1/2023
# mod by Rich Whiffen - 10/27/2024 - 3.0 version of API call
#

"""
This example queries the Open Weather Maps site API to find out the current
weather for your location... and display it on a screen!
if you can find something that spits out JSON data, we can display it
"""
import sys
import time
import board
import busio
import adafruit_adt7410
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pyportal import PyPortal

cwd = ("/"+__file__).rsplit('/', 1)[0] # the current working directory (where this file is)
sys.path.append(cwd)
import openweather_graphics  # pylint: disable=wrong-import-position

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Use cityname, country code where countrycode is ISO3166 format.
# E.g. "New York, US" or "London, GB"
LOCATION = "Arlington County, US"

# Set up where we'll be fetching data from
DATA_SOURCE = "http://api.openweathermap.org/data/3.0/weather?q="+LOCATION
DATA_SOURCE += "&appid="+secrets['openweather_token']
# You'll need to get a token from openweather.org, looks like 'b6907d289e10d714a6e88b30761fae22'
DATA_LOCATION = []
time_counter=0

# Initialize the pyportal object and let us know what data to fetch and where
# to display it
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=DATA_LOCATION,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=0x000000)

# intialize the pyportal  adt7410
i2c_bus = busio.I2C(board.SCL, board.SDA)
adt = adafruit_adt7410.ADT7410(i2c_bus, address=0x48)
adt.high_resolution = True
room_temperature = 50 # start with an above zero temp

#  setting up the hardware snooze/dismiss buttons
switch_dark = DigitalInOut(board.D3)
switch_dark.direction = Direction.INPUT
switch_dark.pull = Pull.UP

switch_light = DigitalInOut(board.D4)
switch_light.direction = Direction.INPUT
switch_light.pull = Pull.UP

#the backlight should start on
light_on = True

gfx = openweather_graphics.OpenWeather_Graphics(pyportal.splash, am_pm=True, celsius=False)

localtile_refresh = None
weather_refresh = None
while True:
    # only query the online time once per hour (and on first run)
    if (not localtile_refresh) or (time.monotonic() - localtile_refresh) > 3600:
        try:
            print("Getting time from internet!")
            pyportal.get_local_time()
            localtile_refresh = time.monotonic()
        except RuntimeError as e:
            print("Some error occured, retrying! -", e)
            continue

    # only query the weather every 10 minutes (and on first run)
    # adding temp sensor to this part
    if (not weather_refresh) or (time.monotonic() - weather_refresh) > 600:
        try:
            value = pyportal.fetch()
            print("Response is", value)
            gfx.display_weather(value)
            weather_refresh = time.monotonic()
            # read the temperature sensor
            room_temperature = adt.temperature
            print("room temp is ", room_temperature)
        except RuntimeError as e:
            print("Some error occured, retrying! -", e)
            continue
    if light_on==False and (not switch_light.value): #light_on=false and button press
        pyportal.set_backlight(1)
        print("turing light on\n")
        light_on= True # set it to trun now
    if light_on==True and (not switch_dark.value): #light_on=True and button press
        pyportal.set_backlight(0)
        print("turing light off\n")
        light_on= False #

    if time_counter>59: #rough estimate for a minute having passed
        time_counter=0 # reset for next loop
        gfx.update_time() # update clock

    time.sleep(1)  # wait 30 seconds before updating anything again
    time_counter+=1 #incremenet time_counter to know if we should update clock next loop
