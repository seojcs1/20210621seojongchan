import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import sleep

mylcd = LCD.lcd()
switch1 = 8
switch2 = 10
led1 = 11
led2 = 12




while True:
    x = input()
    y = len(x)
    print(y)
    if len(x) < 10:   # 숫자 길이가 1~10 까지일떄
        mylcd.lcd_display_string(x,1)
        
    
