from sense_hat import SenseHat
from time import *
from random import *
sense = SenseHat()
import json
import urllib.request
import requests

#!/usr/bin/env python
#COLORS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
r = (255, 0, 0)
g = (0, 193, 138)
b = (0, 0, 255)
lb = (127, 127, 255)
dr = (58, 0, 0)
w = (255, 255, 255)
dg = (0, 127, 91)
y = (255, 255, 0)
lg = (16, 255, 0)
br = (255, 255, 255)
dbr = (255, 170, 0)
idk = (255, 255, 255)
bn = (0, 0, 0)
grey = (137, 137, 137)
#Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Display_Sheets~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hamster_stand = [
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, br, bn, bn,
  bn, bn, grey, dbr, br, br, br, bn,
  bn, br, grey, br, br, dbr, dr, bn,
  bn, grey, dbr, idk, idk, idk, br, dbr,
  bn, bn, dbr, br, bn, dbr, br, bn
  ]
hamster_hop = [
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, br, bn, bn,
  bn, bn, grey, br, br, br, br, bn,
  bn, br, grey, br, br, br, dr, bn,
  bn, grey, dbr, idk, idk, idk, br, dbr,
  bn, bn, br, br, bn, dbr, br, bn,
  bn, bn, bn, bn, bn, bn, bn, bn
  ]
hamster_blink = [ 
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, br, bn, bn,
  bn, bn, grey, dbr, br, br, br, bn,
  bn, br, grey, br, br, dbr, br, bn,
  bn, grey, dbr, idk, idk, idk, br, dbr,
  bn, bn, dbr, br, bn, dbr, br, bn
  ]
hamster_run_1 = [
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, br, bn, bn,
  bn, bn, grey, dbr, br, br, br, bn,
  bn, br, grey, br, br, dbr, dr, bn,
  bn, grey, dbr, idk, idk, idk, br, dbr,
  bn, bn, bn, br, br, bn, br, br
  ]
hamster_run_2 = [
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, bn, bn, bn,
  bn, bn, bn, bn, bn, br, bn, bn,
  bn, bn, grey, dbr, br, br, br, bn,
  bn, br, grey, br, br, dbr, dr, bn,
  bn, grey, dbr, idk, idk, idk, br, dbr,
  bn, br, br, bn, br, br, bn, bn
  ]
hamster_treadmill_1 = [
  bn, bn, bn, bn, br, bn, bn, bn,
  bn, bn, br, br, br, y, bn, bn,
  bn, grey, br, br, br, br, br, bn,
  br, grey, grey, br, br, r, r, r,
  grey, br, br, br, bn, bn, bn, r,
  br, br, br, bn, bn, bn, bn, r,
  bn, br, br, bn, bn, bn, bn, r,
  r, r, r, r, r, r, r, r
  ]
hamster_treadmill_2 = [
  bn, bn, bn, bn, br, bn, bn, bn,
  bn, bn, br, br, br, y, bn, bn,
  bn, grey, br, br, br, br, br, bn,
  br, grey, grey, br, br, r, r, r,
  grey, br, br, br, bn, bn, bn, r,
  br, br, br, bn, bn, bn, bn, r,
  br, br, bn, bn, bn, bn, bn, r,
  r, r, r, r, r, r, r, r
  ]
"""hamster_water_drink_H = [
  w, bn, bn, w, bn, bn, b, lb,
  w, w, w, w, bn, bn, lb, b,
  w, bn, bn, w, bn, bn, b, b,
  w, bn, bn, w, br, bn, b, lb,
  bn, br, grey, br, br, br, bn, b,
  br, br, grey, br, br, dr, bn, w,
  br, grey, idk, idk, idk, br, br, w,
  bn, br, br, bn, br, br, bn, bn
  ]
hamster_water_drink_2 = [
  bn, w, w, bn, bn, bn, lb, b,
  w, bn, bn, w, bn, bn, b, b,
  bn, bn, w, bn, bn, bn, b, lb,
  w, w, w, w, br, bn, b, b,
  bn, br, grey, br, br, br, bn, lb,
  br, br, grey, br, br, dr, bn, w,
  br, grey, idk, idk, idk, br, br, w,
  bn, br, br, bn, br, br, bn, bn
  ]
hamster_water_drink_O = [
  bn, w, w, bn, bn, bn, b, lb,
  w, bn, bn, w, bn, bn, b, b,
  w, bn, bn, w, bn, bn, lb, b,
  bn, w, w, bn, br, bn, b, b,
  bn, br, grey, br, br, br, bn, b,
  br, br, grey, br, br, dr, bn, w,
  br, grey, idk, idk, idk, br, br, w,
  bn, br, br, bn, br, br, bn, bn
  ]"""
  
#Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
run = False
water = False

status = "chillin"
sense.set_rotation(270)
while True:
    try:
        status = str((requests.get("http://piland.socialdevices.io/42/read/1")).text)
        print(status)
    except:
        print("There was an error attempting to read status data from piland")
    if status == "running":
        run = True
    else:
        run = False
    if run == True:
        sense.set_pixels(hamster_run_1)
        sleep(0.2)
        sense.clear()
        sense.set_pixels(hamster_stand)
        sleep(0.2)
        sense.clear()
        sense.set_pixels(hamster_run_2)
        sleep(0.2)
    elif water == True:
        sense.set_pixels(hamster_water_drink_H)
        sleep(0.5)
        sense.clear()
        sense.set_pixels(hamster_water_drink_2)
        sleep(0.5)
        sense.clear()
        sense.set_pixels(hamster_water_drink_O)
        sleep(0.5)
    else:
        sense.set_pixels(hamster_stand)
        sleep(1)
        sense.clear()
        sense.set_pixels(hamster_blink)
        sleep(0.5)
        sense.clear()
        sense.set_pixels(hamster_stand)
        sleep(1)
        sense.clear()
        sense.set_pixels(hamster_hop)
        sleep(0.2)
