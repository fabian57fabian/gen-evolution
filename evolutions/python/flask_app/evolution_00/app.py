
from flask import Flask

app = Flask(__name__)

# New Feature: Displaying current time
from datetime import datetime

@app.route("/")
def hello_world():
    now = datetime.now()
    return "<p>Hello, World! The current time is: {0}</p>".format(now.strftime("%H:%M:%S"))

# Improve efficiency: Use a more efficient way to check if it's the main file
def is_main():
    return __name__ == '__main__' or not hasattr(__import__(__name__), 'is_main')

if is_main():
    app.run()
