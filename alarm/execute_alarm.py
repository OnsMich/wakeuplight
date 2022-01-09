import os
import pickle
import time

import settings


def detect_existing_alarm():
    if os.path.exists(settings.ALARM_FILE_NAME):
        with open(settings.ALARM_FILE_NAME, 'rb') as handle:
            return pickle.load(handle)
    return None


def check_to_wake(alarm: dict):
    """ Check whether it is the right time to start the waking procedure"""
    if correct_time(alarm):
        if correct_sleep_cycle():
            return True
    return False


def correct_sleep_cycle():
    """ Returns True if the movement sensors indicate that victim is in light sleep"""
    return True


def correct_time(alarm: dict):
    """ Returns True if current time is in (alarm_time - interval, interval) """
    return True


def wake_up():
    """ Use LED-lights and possible music to wake the victim"""
    pass


if __name__ == '__main__':
    while True:
        alarm = detect_existing_alarm()
        if alarm:
            time_to_wake = check_to_wake(alarm)
            if time_to_wake:
                wake_up()
                os.remove(settings.ALARM_FILE_NAME)
        time.sleep(settings.ALARM_CHECK_INTERVAL_S)
