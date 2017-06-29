import time
from datetime import datetime
from picamera import PiCamera
import smtplib
from smtplib import SMTP
from smtplib import SMTPException
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from gpiozero import MotionSensor
from gpiozero import Button
import I2C_LCD_driver
import pygame


mylcd = I2C_LCD_driver.lcd() 
pir = MotionSensor(4)
button = Button(17)
camera = PiCamera()
f_time = datetime.now().strftime('%a %d %b @ %H:%M')

#while True:
 #   mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
  #  mylcd.lcd_display_string("Date: %s" %time.strftime("%d:%m:%Y"), 2)
   # time.sleep(0)
    #if button.is_pressed == True or pir.wait_for_motion():
     #   mylcd.lcd_clear()
      #  C().my_method()
            
            
# with picamera.PiCamera() as camera:
#button.wait_for_press()
class C:
    def my_method(self):
        mylcd.lcd_display_string("Ding Dong!", 1)
        mylcd.lcd_display_string(f_time, 2,0)
        time.sleep(2)
        mylcd.lcd_clear()
        camera.rotation = 180
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2)
        camera.capture('photo.jpg')
        camera.stop_preview()

#f_time = datetime.now().strftime('%a %d %b @ %H:%M')

        toaddr = 'p4063103@live.tees.ac.uk'
        me = 'jack.wilkinson3010@gmail.com'
        subject = 'Ding Dong ' + f_time

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        msg.preamble = "Photo @ " + f_time

        fp = open('photo.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        try:
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.ehlo()
            s.starttls()
            s.login(user = 'jack.wilkinson3010@gmail.com',password = 'Lauren1994$')
            s.sendmail(me, toaddr, msg.as_string())
            s.quit
        except SMTPException as error:
            print ("Error: unable to send mail : {err}".format(err=error))
c = C()

while True:
    mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    mylcd.lcd_display_string("Date: %s" %time.strftime("%d:%m:%Y"), 2)
    time.sleep(0)
    if button.is_pressed:
        pygame.mixer.init()
        pygame.mixer.music.load("doorbell.wav")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        mylcd.lcd_clear()
        c.my_method()
    elif pir.value == True:
        mylcd.lcd_clear()
        c.my_method()

