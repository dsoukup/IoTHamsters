from gpiozero import MotionSensor
import time
import datetime

food = 0
pir = MotionSensor(4)

print ("Hi!  This is the food tracker for Nibbles!")
print (now.strftime("%Y - %m - %d %H:%M:%S")

while True:
    pir.wait_for_motion()
    print ("I'm at my foodbowl")
    food += 1
    print (time.time())
    pir.wait_for_no_motion()
    print ("I am not at my foodbowl")
