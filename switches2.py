import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18
door_pin = 23

io.setup(pir_pin, io.IN) #activate input
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP) #activate input with PullUp

wheel_rotations = 0

while True:
    if io.input(pir_pin):
        print("HAMSTER ON THE MOVE!")
    if io.input(door_pin):
        print("WHEEL SWITCH OPEN")
    else:
        wheel_rotations = wheel_rotations + 1
        print("wheel rotations =", wheel_rotations)
    time.sleep(.25)

              