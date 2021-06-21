# smbus library
import smbus

# time library
import time
import I2C_driver as LCD
import RPi.GPIO as GPIO

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

bus = smbus.SMBus(1)

# IC address
address = 0x53

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# ADXL345 init
def init_ADXL345():    
    print('ADXL345 init function')
    bus.write_byte_data(address, 0x2D, 0x08)

# data measure
def measure_acc(adr):    
    acc0 = bus.read_byte_data(address, adr)

    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0

    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    acc = acc * 3.9 / 1000

    return acc


def main():
    print(bus)
    init_ADXL345()
    mylcd = LCD.lcd()
       
    while True:
        mylcd.lcd_clear()
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)
        
        
        if y_acc > 0:
            mylcd.lcd_clear()
            mylcd.lcd_display_string('forward', 1) # 첫번째 LCD 라인
        
        elif z_acc > 0 :
            mylcd.lcd_clear()
            mylcd.lcd_display_string('left', 1)
        elif y_acc < -0.5:
            mylcd.lcd_clear()
            mylcd.lcd_display_string('backword', 1)
        elif z_acc < 0:
            mylcd.lcd_clear()
            mylcd.lcd_display_string('right', 1)
        
            
            
        
        
            
        
        
    
            
        print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
            
        

    
        
if __name__ == '__main__':
    main()