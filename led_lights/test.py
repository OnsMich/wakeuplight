import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, True)
time.sleep(0.05)
GPIO.output(12, False)
time.sleep(0.05)

pwm = GPIO.PWM(12, 50)

pwm.start()

try:
    while True:
        for i in range(50):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(50):
            pwm.ChangeDutyCycle(50 - i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
