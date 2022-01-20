import os
import pickle
import time

import settings
from audio.audio_player import AudioPlayer
from gpio_settings import RED_GPIO
from led_lights.led import LED
import RPi.GPIO as GPIO

_TEST_MODE = True


def detect_existing_alarm():
    alarm_location = f'../{settings.ALARM_FILE_NAME}'
    if os.path.exists(alarm_location):
        with open(alarm_location, 'rb') as handle:
            return pickle.load(handle)
    return None


def time_to_wake(alarm: dict):
    """ Check whether it is the right time to start the waking procedure"""
    if correct_time(alarm):
        if correct_sleep_cycle():
            return True
    return False


def correct_sleep_cycle():
    """ Returns True if the movement sensors indicate that victim is in light sleep"""
    if _TEST_MODE:
        return True
    return True


def correct_time(alarm: dict):
    """ Returns True if current time is in (alarm_time - interval, interval) """
    if _TEST_MODE:
        return True
    return True


def wake_up():
    """ Use LED-lights and music to wake the victim"""
    red_led = LED(RED_GPIO)
    audio_player = AudioPlayer()
    try:
        red_led.turn_on()
        audio_player.play_file()
    except KeyboardInterrupt:
        red_led.turn_off()
        GPIO.cleanup()


if __name__ == '__main__':
    while True:
        alarm = detect_existing_alarm()
        if alarm:
            if time_to_wake(alarm):
                wake_up()
                if _TEST_MODE:
                    break
                os.remove(settings.ALARM_FILE_NAME)
        time.sleep(settings.ALARM_CHECK_INTERVAL_S)
