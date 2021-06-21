import RPi.GPIO as GPIO
import time

switch1 = 10


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch1, GPIO.IN)

LED = 12
a = 0


def main():
    a = 0
    b = 0
    GPIO.setup(LED, GPIO.OUT)


    while 1:
        
        
        if  GPIO.input(switch1) == GPIO.HIGH:
            a = 1
            GPIO.output(LED,GPIO.HIGH)
            time.sleep(1)
            
        if (GPIO.input(switch1) == GPIO.HIGH and a == 1):
            a = 0
            GPIO.output(LED,GPIO.LOW)
            time.sleep(1)
               
                
            
              
  

if __name__ == '__main__':
    main()

            

