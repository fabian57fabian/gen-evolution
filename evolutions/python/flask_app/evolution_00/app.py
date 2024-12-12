
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    now = datetime.now().strftime("%H:%M:%S")
    return "<p>Hello, World! The current time is: {0}</p>".format(now)

def is_main():
    return hasattr(sys.modules[__name__], '__file__')

if is_main():
    app.run()
