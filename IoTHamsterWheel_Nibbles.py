# adaptations by Martie Schenghaust, Lauren Bryant, and Deanna Soukup 2019
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
import schedule
from math import pi
import paho.mqtt.publish as publish
import RPi.GPIO as io
import requests
from twython import Twython

# The hamster's name
hamsterName = "Nibbles"

if hamsterName == "Nibbles":
    # The Channel ID for the ThingsSpeak channel for Nibbles
    channelID = "635861"
    # The Write API key of the ThingsSpeak channel for Nibbles
    apiKey = "0QM9D4TF0YZWKO9F"
    # The other hamster's name
    otherHamsterName = "Bits"
    #otherChannelID is bitsThe Channel ID for the ThingsSpeak channel for Bits
    otherChannelID = "651391"
    
    
if hamsterName == "Bits":
    # The Channel ID for the ThingsSpeak channel for Bits
    channelID = "651391"
    # The Write API key of the ThingsSpeak channel for Bits
    apiKey = "RV9EWRWEZPOHCFNM"
    # The other hamster's name
    otherHamsterName = "Nibbles"
    #otherChannelID is bitsThe Channel ID for the ThingsSpeak channel for Nibbles
    otherChannelID = "635861"
    

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

# The Hostname of the ThinSpeak MQTT service
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

# Circumferance of hamster wheel in miles
# 16.5 cm diameter wheel * pi /100000
wheelsize = (16.51*pi/100000.)*0.62137

# Number of wheel rotations
# reset to 0 every minute
rotations = 0

# Distance covered in hamsterwheel
distance = 0

# Daily distance
# Reset to 0 every day at 0:00
dailyDistance = float(requests.get('https://api.thingspeak.com/channels/' + channelID + '/fields/2/last.txt').text)
if dailyDistance < 0.0:
    dailyDistance = 0.0

# this is his overall top distance ran ever
top_distance = 0.0

# Speed
speed = 0.0

#Average Speed
#Average Speed Calulate in a minute
averageSpeed = 0.0

# Set the starttime to now
starttime = datetime.datetime.now()

# Reset the measurements each minute
def resetValues():
    global distance
    global speed
    global rotations
    distance = 0
    speed = 0
    rotations = 0
    
    
def resetDailyValues():
    global dailyDistance
    dailyDistance = 0

def set_top_distance():
    global top_distance
    if dailyDistance > top_distance:
        top_distance = dailyDistance

# Send IoT message to Thingspeak
def sendThingSpeakMessage():
    # build the payload string
    tPayload = "field1=" + str(rotations) + "&field2=" + str(dailyDistance)
    resetValues()
    # attempt to publish this data to the topic
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
        print("Published data to ThingSpeak: " + str(rotations) + " rotations, " + str(dailyDistance) + " miles.")
    except:
        print("There was an error while publishing the data.")
        
# Send a message every minute to ThingSpeak
schedule.every().minutes.do(sendThingSpeakMessage)

'''
def sendTestTwitterMessage():
    #Nibbles test tweet
    try:
        testMessage = "Hi! It's " + hamsterName + "! I am at " + str(dailyDistance) + " miles so far today!"
        twitter.update_status(status=testMessage)
        print("Tweeted %s" % testMessage)
    except:
        print("There was an error while Tweeting.")
        '''


# Send IoT message to Twitter
def sendTwitterMessage():
    try:
        message = "Hi! It's " + hamsterName + "! I ran " + str(dailyDistance) + " miles today!"
        twitter.update_status(status=message)
        print("Tweeted %s" % message)
    except:
        print("There was an error while Tweeting.")

#If Hamster is Nibbles, Send Message at 3:00 PM to Twitter
if hamsterName == "Nibbles":
    schedule.every().day.at("15:00").do(sendTwitterMessage)

#If Hamster is Bits, Send Message at 3:01 PM to Twitter
if hamsterName == "Bits":
    schedule.every().day.at("15:01").do(sendTwitterMessage)

# set the top_distance vaules at 3:02 PM
schedule.every().day.at("15:02").do(set_top_distance)

# Reset the daily values at 3:04 PM 
schedule.every().day.at("15:03").do(resetDailyValues)


# Function to calculate the current speed of the hamster wheel
def calculateSpeed(spintime):
    seconds = spintime.days * 24 * 60 * 60 + spintime.seconds + spintime.microseconds / 1000000.
    return wheelsize / (seconds/60./60.)

#Print the hamster's name to the console
print("Hi, this is a tracker for " + hamsterName)

#optional Twitter test upon restart
#sendTestTwitterMessage()

#sets the lastInput of the reed switch to a value of 1 when the script runs
lastInput = 1

#when the script runs,..
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
            # Calculating the speed based on the spintime
            speed = calculateSpeed(spintime)
            # Calculating the distance covered
            distance = distance + wheelsize
            dailyDistance = dailyDistance + wheelsize
            # Calculating the amount of rotations
            rotations += 1
            # Print to console and sleep
            print ('rotations =', rotations, 'rotations.  dailyDistance = ', dailyDistance, 'miles' )
            lastInput = 1
        if(io.input(wheelpin) == 0):
            lastInput = 0
        #the time interval for checking the sensor is 0.01 seconds
        time.sleep(0.01)


