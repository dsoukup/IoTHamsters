from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
    print ("Test")
    pir.wait_for_motion()
    print ("Hamham")
    pir.wait_for_no_motion()
