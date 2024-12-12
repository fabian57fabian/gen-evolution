
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(email, message)
        return {'message': f'Name: {name}, Email: {email}, Message: {message}', 'success': True}, 200
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        data = request.get_json(force=True)
        success = process_about_form(data)
        return {'success': success}, 201
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json(force=True)
    process_contact_form(data)
    return {'submitted': True}, 202

@app.route('/newfeature', methods=['GET'])
def new_feature():
    user_name = request.args.get('user')
    if user_name:
        welcome_message = f"Hello, {user_name}! This is your personalized page."
    else:
        welcome_message = "Welcome to our website!"
    return {'welcome_message': welcome_message}

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

def send_email(email, message):
    import smtplib
    smtplib.SMTP('smtp.example.com', 587).sendmail('your_email@example.com', email, message)

def process_about_form(form_data):
    # Efficient processing logic here
    return True

def process_contact_form(form_data):
    # Improved contact form processing
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
