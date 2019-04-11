# adaptations by Martie Schenghaust, Lauren Bryant, Kodey Buxbaum, and Deanna Soukup 2019
#
# Sources and Inspiration:
#
# Our inspiration:
# Nichole Howard 2018
# https://www.instructables.com/id/Project-Floofball-an-IoT-Hamster-Wheel/
# https://github.com/NHorward/IoTHamsterWheel
#
# Nichole's Inspiration:
# http://www.instructables.com/id/Track-How-Far-Your-Hamster-Runs/
#
# ThingSpeak:
# https://community.thingspeak.com/tutorials/update-a-thingspeak-channel-using-mqtt-on-a-raspberry-pi/
#
# Magnetic door sensor:
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement/overview
#
# Scheduler:
# https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately
# https://apscheduler.readthedocs.io/en/latest/userguide.html#configuring-the-scheduler
# https://schedule.readthedocs.io/en/stable/
#
# Autorun script on startup of Raspberry Pi:
# https://www.raspberrypi.org/documentation/linux/usage/rc-local.md


# Import libraries
from __future__ import print_function
import time
import datetime
from datetime import timedelta
import schedule
from math import pi
import paho.mqtt.publish as publish
import RPi.GPIO as io
import requests

# The hamster's name
hamsterName = "Nibbles"

#Setup the pins of the RaspberryPi
io.setmode(io.BCM)
# Pin for the wheel
wheelpin = 23
# Setup wheel pin
io.setup(wheelpin, io.IN, pull_up_down=io.PUD_UP)

#when the script runs,..

#Print the hamster's name to the console
print("Hi, this is the 'Running or Naw' data for " + hamsterName)

#Set the name of Piland Room #42 Slot #1
requests.get("http://piland.socialdevices.io/42/write/1?name=Bits+the+Hamster")

#sets the lastInput of the reed switch to a value of 1 when the script runs
lastInput = 1

#declare and initialize the starttime and endtime
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
running = False
new_not_running = True
new_running = True

while True:
        # Check the pending scheduled tasks
        schedule.run_pending()
    
        # When the magnet passes the magnet reed switch, one rotation has happened
        if (io.input(wheelpin) == 1) and (lastInput == 0):
            # The end of the rotation is now
            endtime = datetime.datetime.now()
            # The time spent spinning was the endtime - starttime
            spintime = endtime - starttime
            # New starttime is the endtime
            starttime = endtime
            # Print to console
            print(hamsterName + " is Running")
            if new_running == True:
                try:
                    requests.get("http://piland.socialdevices.io/42/write/2?value=running")
                except:
                    print("There was an error when posting 'is Running' data to Piland")
                new_running = False
                new_not_running = True
            lastTimeRunning = endtime
            lastInput = 1
        if(io.input(wheelpin) == 0):
            lastInput = 0
        currentTime = datetime.datetime.now()
        max_delay = datetime.timedelta(seconds=5)
        nowTime = datetime.datetime.now()
        if nowTime - endtime > max_delay:
            print(hamsterName + " is Not Running")
            if new_not_running == True:
                try:
                    requests.get("http://piland.socialdevices.io/42/write/2?value=chillin")
                except:
                    print("There was an error when posting 'is Not Running' data to Piland")
                new_not_running = False
                new_running = True
        #the time interval for checking the sensor is 0.01 seconds
        time.sleep(.01)
        
