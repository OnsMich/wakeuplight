from pywebio.input import *
from pywebio import start_server
from pywebio.output import put_text


def check_interval(input_interval):
    """ Double validation on interval. Should never be triggered due to slider"""
    if input_interval < 0:
        return 'Interval should be larger than 0'
    if input_interval > 60:
        return 'This seems kinda weird fam'


def app():
    put_text("Please enter desired wake-up time and the start-up interval")
    input_alarm = input_group("Set Alarm", [
        input('Desired wake-up time', name='wake_time', type=TIME),
        slider('Set interval', name='interval_m', value=30, min_value=0, max_value=60, step=1, validate=check_interval)
    ])


if __name__ == '__main__':
    start_server(app, port=2304, debug=True)
