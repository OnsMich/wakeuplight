import time
import RPi.GPIO as GPIO

import settings
from gpio_settings import RED_GPIO, GREEN_GPIO, BLUE_GPIO


class LED(object):
    def __init__(self, gpio_nr):
        GPIO.setmode(GPIO.BCM)
        self.gpio_nr = gpio_nr
        GPIO.setup(self.gpio_nr, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_nr, settings.HERTZ)

    def turn_on(self):
        GPIO.output(self.gpio_nr, True)

    def turn_off(self):
        GPIO.output(self.gpio_nr, False)

    def fade_on(self, duration_sec: int = 1):
        sleeptime = duration_sec / settings.PWM_STEPS
        self.pwm.start()
        try:
            for i in range(settings.PWM_STEPS):
                self.pwm.ChangeDutyCycle(i)
                time.sleep(sleeptime)
        except KeyboardInterrupt:
            pass
        self.pwm.stop()

    def fade_off(self, duration_sec: int = 1):
        sleeptime = duration_sec / settings.PWM_STEPS
        self.pwm.start()
        try:
            for i in range(settings.PWM_STEPS):
                self.pwm.ChangeDutyCycle(settings.PWM_STEPS - i)
                time.sleep(sleeptime)
        except KeyboardInterrupt:
            pass
        self.pwm.stop()

    def slow_blinking(self):
        try:
            while True:
                self.fade_on()
                self.fade_off()
        except KeyboardInterrupt:
            pass

    def blink(self, speed_sec: float = 0.1):
        try:
            while True:
                self.turn_on()
                time.sleep(speed_sec)
                self.turn_off()
                time.sleep(speed_sec)
        except KeyboardInterrupt:
            pass
