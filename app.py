
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        if not name or not email or not message:
            return jsonify({'error': 'All fields are required.'}), 400
        send_email(email, message)
        return redirect('/success')
    return render_template('home.html')

@app.route('/about', methods=['POST'])
def about():
    data = request.json
    keys = ['key1', 'key2']
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Missing {key} key.'}), 400
    success = process_data(data)
    if success:
        return jsonify({'success': True}), 201
    else:
        return jsonify({'error': 'Data processing failed.'}), 400

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    missing_fields = [field for field in ['name', 'email', 'message'] if field not in data]
    if missing_fields:
        return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}', 'submitted': False}), 400
    
    for field in ['name', 'email', 'message']:
        if not data[field]:
            return jsonify({'error': f'Please fill in the {field} field.', 'submitted': False}), 400
    
    success = validate_data(data)
    if success:
        return jsonify({'submitted': True}), 202
    else:
        return jsonify({'submitted': False}), 400

@app.route('/newfeature', methods=['GET'])
def new_feature():
    user = request.args.get('user')
    message = get_message(user)
    return jsonify({'message': message}), 200

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

def send_email(email, message):
    # Your email sending logic here
    pass

def process_data(data):
    # Efficient data processing
    return True

def validate_data(data):
    # Improved validation logic
    return True

def get_message(user=None):
    if user:
        return f"Hello, {user}! Welcome to the new feature."
    return "Explore the new feature!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
