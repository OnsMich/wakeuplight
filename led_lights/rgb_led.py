import time

import settings
from gpio_settings import RED_GPIO, GREEN_GPIO, BLUE_GPIO
from led_lights.led import LED


class RGBLED(object):
    def __init__(self):
        self.red = LED(RED_GPIO)
        self.green = LED(GREEN_GPIO)
        self.blue = LED(BLUE_GPIO)

    def turn_on(self):
        self.red.turn_on()
        self.green.turn_on()
        self.blue.turn_on()

    def turn_off(self):
        self.red.turn_off()
        self.green.turn_off()
        self.blue.turn_off()

    def fade_on(self, duration_sec: int = 1):
        sleeptime = duration_sec / settings.PWM_STEPS

        self.red.pwm.start()
        self.green.pwm.start()
        self.blue.pwm.start()

        try:
            for i in range(settings.PWM_STEPS):
                self.red.pwm.ChangeDutyCycle(i)
                self.green.pwm.ChangeDutyCycle(i)
                self.blue.pwm.ChangeDutyCycle(i)
                time.sleep(sleeptime)
        except KeyboardInterrupt:
            pass
        self.red.pwm.stop()
        self.green.pwm.stop()
        self.blue.pwm.stop()

    def fade_off(self, duration_sec: int = 1):
        sleeptime = duration_sec / settings.PWM_STEPS

        self.red.pwm.start()
        self.green.pwm.start()
        self.blue.pwm.start()

        try:
            for i in range(settings.PWM_STEPS):
                self.red.pwm.ChangeDutyCycle(settings.PWM_STEPS - i)
                self.green.pwm.ChangeDutyCycle(settings.PWM_STEPS - i)
                self.blue.pwm.ChangeDutyCycle(settings.PWM_STEPS - i)
                time.sleep(sleeptime)
        except KeyboardInterrupt:
            pass
        self.red.pwm.stop()
        self.green.pwm.stop()
        self.blue.pwm.stop()

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
