#second

from gpiozero import MotionSensor
import time
import datetime
from datetime import date
from twython import Twython
import schedule
import requests

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

meal = hamsterName
breakfast = 0
lunch = 0
dinner = 0
snacks = 0
pir = MotionSensor(4)
now = datetime.datetime.now()

tweeted = False

# Send IoT message to Twitter
def sendTwitterMessage():
    try:
        now = datetime.datetime.now()
        if int(meal) <= 0:
            message = "It's me, " + hamsterName + ". I didn't eat " + ToD + " today. I am hungry."
        else:
            "It's me, " + hamsterName + ". I ate " + ToD + " " + meal + " times today! I was hungry."
        twitter.update_status(status=message)
        print("Tweeted %s" % message)
        tweeted = True
    except:
        now = datetime.datetime.now()
        print("There was an error while Tweeting.")

print ("Hi!  This is the food tracker for Nibbles!")
print (date.today())
def u():
    now = datetime.datetime.now()
    if now.strftime("%H:%M:%S") >= now.strftime("05:00:00") and now.strftime("%H:%M:%S") <= now.strftime("11:00:00"):
        ToD = "snacks"
        meal = str(snacks)
    elif now.strftime("%H:%M:%S") >= now.strftime("11:00:01") and now.strftime("%H:%M:%S") <= now.strftime("15:00:00"):
        ToD = "breakfast"
        meal = str(breakfast)
    elif now.strftime("%H:%M:%S") >= now.strftime("15:00:01") and now.strftime("%H:%M:%S") <= now.strftime("19:00:00"):
        ToD = "lunch"
        meal = str(lunch)
    elif now.strftime("%H:%M:%S") >= now.strftime("19:00:01") and (now.strftime("%H:%M:%S") <= now.strftime("24:59:59") or now.strftime("%H:%M:%S") <= now.strftime("4:59:59")):
        ToD = "dinner"
        meal = str(dinner)

schedule.every().day.at("05:00").do(u)
schedule.every().day.at("11:01").do(u)
schedule.every().day.at("15:01").do(u)
schedule.every().day.at("19:01").do(u)
schedule.every().day.at("04:59").do(sendTwitterMessage)
schedule.every().day.at("10:59").do(sendTwitterMessage)
schedule.every().day.at("14:59").do(sendTwitterMessage)
schedule.every().day.at("18:59").do(sendTwitterMessage)

while True:
    pir.wait_for_motion()
    now = datetime.datetime.now()
    print ("I'm at my foodbowl")
    print (now.strftime("%H:%M:%S"))
    print (datetime.datetime.now())
    if now.strftime("%H:%M:%S") >= now.strftime("05:00:00") and now.strftime("%H:%M:%S") <= now.strftime("11:00:00"):
        snacks = 0
        breakfast += 1
        print (breakfast)
    if now.strftime("%H:%M:%S") >= now.strftime("11:00:01") and now.strftime("%H:%M:%S") <= now.strftime("15:00:00"):
        breakfast = 0
        lunch += 1
        print (lunch)
    if now.strftime("%H:%M:%S") >= now.strftime("15:00:01") and now.strftime("%H:%M:%S") <= now.strftime("19:00:00"):
        lunch = 0
        dinner += 1
        print (dinner)
    if now.strftime("%H:%M:%S") >= now.strftime("19:00:01") and (now.strftime("%H:%M:%S") <= now.strftime("24:59:59") or now.strftime("%H:%M:%S") <= now.strftime("4:59:59")):
        dinner = 0
        snacks += 1
        print (snacks)
    pir.wait_for_no_motion()
    print ("I am not at my foodbowl")


#if int(now.strftime("%H%M%S")) >= 60000 and int(now.strftime("%H%M%S") <= 115959: breakfast += 1 print ("Breakfast: " + breakfast)
