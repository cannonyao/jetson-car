import time
import RPi.GPIO as GPIO
import threading
import traitlets
from traitlets.config.configurable import HasTraits

GPIO.setmode(GPIO.BCM)
#IN1 = 12
#IN2 = 16
#IN3 = 20
#IN4 = 21

IN1 = 16
IN2 = 12
IN3 = 21
IN4 = 20

GPIO.setup(IN1,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(IN2,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(IN3,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(IN4,GPIO.OUT, initial=GPIO.HIGH)



class wheels(HasTraits):
    def __init__(self):
        self.max_dt = 0.03
        self.max_speed = 0.03
        self.power = 0
        self.left_speed = 0
        self.right_speed = 0
        
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.LOW)

        threading.Thread(target=self.left_wheel,args=()).start()
        threading.Thread(target=self.right_wheel, args=()).start()
        
        

    def left_wheel(self):
        while True:
            if self.power:
                dt_low = self.max_dt -self.left_speed
                dt_low = 0.01
                GPIO.output(IN2,GPIO.HIGH)
                time.sleep(self.left_speed)
                GPIO.output(IN2,GPIO.LOW)
                time.sleep(dt_low)

    def right_wheel(self):
        while True:
            if self.power:
                dt_low = self.max_dt - float(self.right_speed)

                GPIO.output(IN4,GPIO.HIGH)
                time.sleep(self.right_speed)
                GPIO.output(IN4,GPIO.LOW)
                time.sleep(dt_low)


    def stop():
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.LOW)

if __name__ =="__main__":
    test = wheels()
    test.power = 1
    test.left_speed = 0.01
    test.right_speed = 0.03
