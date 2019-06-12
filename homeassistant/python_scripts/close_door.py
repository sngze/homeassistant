import RPi.GPIO as GPIO
import time

pin_pwm = 23
frequency = 30

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_pwm, GPIO.OUT)

p = GPIO.PWM(pin_pwm, frequency)
p.start(0)

p.ChangeDutyCycle(1)
time.sleep(1)

