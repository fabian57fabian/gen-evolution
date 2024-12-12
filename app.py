
from flask import Flask, request, jsonify

app = Flask(__name__)

# New feature: Log the requests for debugging
@app.after_request
def improve_logging(response):
    print("Received request - Path: {}, Status: {}, Content: {}".format(
        response.request.path, response.status_code, response.get_data()))
    return response

@app.route('/')
def efficient_hello():
    return jsonify({'hello': 'world'}), 200

@app.route('/greet', methods=['GET'])
def greet_efficient_get():
    name = request.args.get('name')
    if name:
        return jsonify({'message': f'Hello, {name}!'}), 200
    else:
        return jsonify({'error': 'Name parameter is required'}), 400  # Improved error message

@app.route('/greet', methods=['POST'])
def greet_efficient_post():
    data = request.get_json()
    if 'name' in data:
        return jsonify({'message': f'Hello, {data["name"]}!'}), 201
    else:
        return jsonify({'error': 'Name field is missing in the JSON body'}), 400  # Improved error message

if __name__ == '__main__':
    app.run()
