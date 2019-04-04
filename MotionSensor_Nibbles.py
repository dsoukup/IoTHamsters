from gpiozero import MotionSensor
import time

pir = MotionSensor(4)

print ("Hi!  This is the food tracker for Nibbles!")

while True:
    pir.wait_for_motion()
    print ("I'm at my foodbowl")
    pir.wait_for_no_motion()
    print ("I am not at my foodbowl")


