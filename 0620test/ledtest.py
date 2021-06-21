import RPi.GPIO as GPIO
from time import sleep



GPIO.setmode(GPIO.BOARD) #보드 방식으로 사용하겠다 

LED = 11     #엘이디 11번 사용
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(12,GPIO.OUT,initial = GPIO.LOW)


while True:
    GPIO.output(LED,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    sleep(1)
    GPIO.output(LED,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    sleep(1)

   

