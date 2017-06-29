from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
while True:
     pir.wait_for_motion()
     print("motion detected!")
     pir.wait_for_no_motion()
     print("no motion")

