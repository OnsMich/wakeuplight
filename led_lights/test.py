import RPi.GPIO as GPIO
import time

gpio_nr = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_nr, GPIO.OUT)
print('start')
GPIO.output(gpio_nr, True)
time.sleep(15)
GPIO.output(gpio_nr, False)
time.sleep(0.05)

pwm = GPIO.PWM(gpio_nr, 50)

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
