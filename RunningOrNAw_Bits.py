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
from twython import Twython

# The hamster's name
hamsterName = "Bits"

# The Channel ID for the ThingsSpeak channel
channelID = "651391"

# The Write API key of the ThingsSpeak channel
apiKey = "RV9EWRWEZPOHCFNM"
#Bits read api key is ZW8R77Q2DV8C2RL6

#  MQTT Connection Methods
# Set useUnsecuredTCP to True to use the default MQTT port of 1883
# This type of unsecured MQTT connection uses the least amount of system resources.
useUnsecuredTCP = False

# Set useUnsecuredWebSockets to True to use MQTT over an unsecured websocket on port 80.
# Try this if port 1883 is blocked on your network.
useUnsecuredWebsockets = False

# Set useSSLWebsockets to True to use MQTT over a secure websocket on port 443.
# This type of connection will use slightly more system resources, but the connection
# will be secured by SSL.
useSSLWebsockets = True

# The Hostname of the ThingSpeak MQTT service
mqttHost = "mqtt.thingspeak.com"

# Set up the connection parameters based on the connection type
if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443

# Create the topic string for ThingSpeak
topic = "channels/" + channelID + "/publish/" + apiKey

#Twitter Settings

#This is the consumer key and acessToken for Twitter
consumer_key = 'tjtfUlxkJWLPF240iTdpWJsGB'
consumer_secret = 'n8GjquCU8fvBvhreAPmRUujbe34uAa8eIrUVM66DOf2HyiV3xd'
access_token = '1066570821773287431-rlEjHoKX0cK1ifOP5LScP21SIn1mvl'
access_token_secret = 'PuRSZQrlq4GYr2BWY7pKjr8lV0NgG624fNyoC5mZzVGFT'
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

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
                    requests.get("http://piland.socialdevices.io/42/write/1?value=running")
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
                    requests.get("http://piland.socialdevices.io/42/write/1?value=chillin")
                except:
                    print("There was an error when posting 'is Not Running' data to Piland")
                new_not_running = False
                new_running = True
        #the time interval for checking the sensor is 0.01 seconds
        time.sleep(.01)
        
