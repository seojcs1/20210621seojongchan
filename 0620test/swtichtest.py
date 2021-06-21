import RPi.GPIO as GPIO
from time import *


switch1 = 8
switch2 =10
led1 = 11
led2 = 12


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)


while True:
	if ( GPIO.input(switch1) and GPIO.input(switch2) ) == GPIO.HIGH:
		print("on")
		GPIO.output(led1,GPIO.HIGH)
		GPIO.output(led2,GPIO.HIGH)
	
	elif ( GPIO.input(switch1) and GPIO.input(switch2) ) == GPIO.LOW:
		print("off")
		GPIO.output(led1,GPIO.LOW)
		GPIO.output(led2,GPIO.LOW)
		