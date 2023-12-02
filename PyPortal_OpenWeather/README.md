OpenWeather App for the PyPortal


This is my version of this project:

[https://learn.adafruit.com/pyportal-weather-station](https://learn.adafruit.com/pyportal-weather-station)

This page is mostly just notes and reminders for myself, not meant for external consumption.  I work on this in fits and starts and go long periods between touching this.

My initial purpose was just to make it work.
It connects to my wifi, has my location and weather API key to get OpenWeather

LINKS:  
[https://circuitpython.org/board/pyportal/](https://circuitpython.org/board/pyportal/) the circuitPython build for the pyportal. Looks like 5.3 is latest but 6.0 is alpha as of 7/12/2020.





Next steps, building on this:

* I'd like to be able to turn the backlight of the portal on and off with
a touch of the screen - It'd be annoying to have it on my night stand with
the light always on.

* I'd like to be able to read the on-board temperature sensor and display the inside and outside temps. I think to get this all on the screen I'll have to customize the graphics to make them smaller to give me more real estate to print things.


7/12/2020 work notes - getting arduino and git set up on my new laptop.  The
whole USB-C connector thing is harshing my mello.  I hate that I have to buy
all new stuff to go with the laptop.  Oh well.


12/1/2023 work notes - after seeing the version of this for the [Adafruit PyPortal Titano](https://www.adafruit.com/product/4444) I copied the idea from the titano implementation that has [STEMMA Wired Tactile Push-Buttons](https://www.adafruit.com/product/4431) to do fancy stuff.  I that idea to pyportal.set_backlight(0) to shut off the light (and 1 to turn back on)