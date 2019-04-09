from gpiozero import MotionSensor
import time
import datetime
from datetime import date
from twython import Twython

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

hamsterName = "Nibbles"

breakfast = 0
lunch = 0
dinner = 0
snacks = 0
now = datetime.datetime.now()
pir = MotionSensor(4)

tweeted = False

# Send IoT message to Twitter
def sendTwitterMessage():
    try:
        message = "It's me, " + hamsterName + ". I ate " + ToD + " times today! I was hungry"
        twitter.update_status(status=message)
        print("Tweeted %s" % message)
        tweeted = True
    except:
        print("There was an error while Tweeting.")

print ("Hi!  This is the food tracker for Nibbles!")
print (date.today())

while True:
    pir.wait_for_motion()
    print ("I'm at my foodbowl")
    print (now.strftime("%H:%M:%S"))
    if now.strftime("%H:%M:%S") >= now.strftime("05:00:00") and now.strftime("%H:%M:%S") <= now.strftime("11:00:00"):
        if tweeted == False:
            ToD = "snacks"
            sendTwitterMessage()
        breakfast += 1
            snacks = 0
    if now.strftime("%H:%M:%S") >= now.strftime("11:00:01") and now.strftime("%H:%M:%S") <= now.strftime("15:00:00"):
        if tweeted == False:
            ToD = "breakfast"
            sendTwitterMessage()
        lunch += 1
            breakfast = 0
    if now.strftime("%H:%M:%S") >= now.strftime("15:00:01") and now.strftime("%H:%M:%S") <= now.strftime("19:00:00"):
        if tweeted == False:
            ToD = "lunch"
            sendTwitterMessage()
        dinner += 1
            lunch = 0
    if now.strftime("%H:%M:%S") >= now.strftime("19:00:01") and (now.strftime("%H:%M:%S") <= now.strftime("24:59:59") or now.strftime("%H:%M:%S") <= now.strftime("4:59:59")):
        if tweeted == False:
            ToD = "dinner"
            sendTwitterMessage()
        snacks += 1
            dinner = 0
    pir.wait_for_no_motion()
    if now.strftime("%H:%M:%S") == now.strftime("05:00:00") or now.strftime("%H:%M:%S") == now.strftime("11:00:01") or now.strftime("%H:%M:%S") == now.strftime("15:00:01") or now.strftime("%H:%M:%S") == now.strftime("19:00:01"):
        tweeted = False
    print ("I am not at my foodbowl")


#if int(now.strftime("%H%M%S")) >= 60000 and int(now.strftime("%H%M%S") <= 115959: breakfast += 1 print ("Breakfast: " + breakfast)
