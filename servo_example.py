import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def paperRollers(isOn):
    try:
        if(isOn):
            p.ChangeDutyCycle(49)
        else:
            p.stop()
        
    except KeyboardInterrupt:
        GPIO.cleanup()

def cleanup_gpio():
    GPIO.cleanup();


paperRollers(True)
while(1):
    pass