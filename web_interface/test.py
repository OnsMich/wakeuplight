# Start with simple PyWebIO web app
# If it proves to be insufficient, then switch to Django(?)

from pywebio.input import textarea, input
from pywebio import start_server
from pywebio.output import put_text


def app():
    text = textarea("Please insert the text for your PDF file",
                    placeholder="Type anything you like",
                    required=True)

    save_location = input("What is the name of your PDF file?", required=True)
    put_text("Congratulations! A PDF file is generated for you.")


if __name__ == '__main__':
    start_server(app, port=36535, debug=True)