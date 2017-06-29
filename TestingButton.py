from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.rotation = 180
camera.start_preview()
button.wait_for_press()
sleep(3)
camera.capture('/home/pi/image9.jpg')
camera.stop_preview()
