
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'hello': 'world'})

@app.route('/greet', methods=['GET'])
def greet_get():
    name = request.args.get('name')
    if name:
        return jsonify({'message': f'Hello, {name}!'}), 200
    else:
        return jsonify({'error': 'Name parameter is missing'}), 400

@app.route('/greet', methods=['POST'])
def greet_post():
    data = request.get_json()
    if 'name' in data:
        return jsonify({'message': f'Hello, {data["name"]}!'}), 201
    else:
        return jsonify({'error': 'Name field is missing'}), 400

if __name__ == '__main__':
    app.run()
