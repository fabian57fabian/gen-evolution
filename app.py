
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'hello': 'world'}

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if name:
        return f'Hello, {name}!', 200
    else:
        return 'Name parameter is missing.', 400

@app.route('/greet', methods=['POST'])
def greet_post():
    name = request.form['name']
    if name:
        return f'Hello, {name}!', 201
    else:
        return 'Name field is missing.', 400

if __name__ == '__main__':
    app.run()
