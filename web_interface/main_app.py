from pywebio.input import *
from pywebio import start_server
from pywebio.output import *
from pywebio.session import *
import pickle
import os

ALARM_FILE_NAME = 'alarm.pkl'


def check_interval(input_interval):
    """ Double validation on interval. Should never be triggered due to slider"""
    if input_interval < 0:
        return 'Interval should be larger than 0'
    if input_interval > 60:
        return 'This seems kinda weird fam'


def show_data_entry() -> dict:
    put_scope(name='data_entry')
    put_text("Please enter desired wake-up time and the start-up interval", scope='data_entry')
    input_alarm = input_group("Set Alarm", [
        input('Desired wake-up time', name='wake_time', type=TIME, scope='data_entry'),
        slider('Set interval', name='interval_m', value=30, min_value=0, max_value=60, step=1, validate=check_interval,
               scope='data_entry')
    ])
    remove(scope='data_entry')
    return input_alarm


def show_cancel_alarm_option(input_alarm: dict) -> None:
    put_scope(name='cancel_alarm')
    put_text(f"Your alarm is set to {input_alarm['wake_time']} with an interval of {input_alarm['interval_m']} minutes",
             scope='cancel_alarm')
    put_button("Cancel Alarm", onclick=remove_set_alarm, scope='cancel_alarm')


def remove_set_alarm():
    os.remove(ALARM_FILE_NAME)
    reload_page()


def reload_page():
    run_js('window.location.reload()')


def set_alarm(input_alarm: dict):
    with open(ALARM_FILE_NAME, 'wb') as handle:
        pickle.dump(input_alarm, handle, protocol=pickle.HIGHEST_PROTOCOL)


def app():
    if os.path.exists(ALARM_FILE_NAME):
        with open(ALARM_FILE_NAME, 'rb') as handle:
            input_alarm = pickle.load(handle)
    else:
        input_alarm = show_data_entry()
        set_alarm(input_alarm)

    show_cancel_alarm_option(input_alarm)


if __name__ == '__main__':
    start_server(app, port=2304, debug=True)
