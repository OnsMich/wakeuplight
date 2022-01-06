from pywebio import start_server
from web_interface.main_app import app

if __name__ == '__main__':
    start_server(app, port=2304, debug=True)
