import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

BOTTOM, MIDDLE, TOP = 0.5, 1.44, 2.4
def setservo(dig):
    pal = 0
    if dig == 0:
        pal = MIDDLE
    elif dig < 0:
        k = (MIDDLE - BOTTOM)/90
        pal = MIDDLE + k*dig
    elif dig > 0:
        k = (TOP - MIDDLE)/90
        pal = MIDDLE + k*dig
    
    servo.ChangeDutyCycle(pal/20*100)

setservo(-90)
time.sleep(1.0)
setservo(-45)
time.sleep(1.0)
setservo(0)
time.sleep(1.0)
setservo(45)
time.sleep(1.0)
setservo(90)
time.sleep(1.0)

GPIO.cleanup()
