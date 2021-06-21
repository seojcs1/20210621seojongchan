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

    PWM_LED= GPIO.PWM(LED, 50)
    PWM_LED.start(0)

    while 1:
        
        
        if  GPIO.input(switch1) == GPIO.HIGH:
            a = 1
            PWM_LED.ChangeDutyCycle(0)
            time.sleep(1)
          
        if (GPIO.input(switch1) == GPIO.HIGH and a == 1):
            PWM_LED.ChangeDutyCycle(50)
            b = 1
            time.sleep(1)
            
        if (GPIO.input(switch1) == GPIO.HIGH and b == 1):
            a=0
            b=0
            PWM_LED.ChangeDutyCycle(100)
            time.sleep(1)
            
              
            
                
                
                    
                    
                
                
                
        
        
            

if __name__ == '__main__':
    main()