
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'Hello': 'World'}

@app.route('/greet')
def greet():
    name = request.args.get('name')
    if name:
        return f'Hello, {name}!'
    return 'Please provide a name parameter.'

if __name__ == '__main__':
    app.run()
