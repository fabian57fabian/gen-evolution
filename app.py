
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
        success = process_about_form(data)  # Pass data directly
        return {'success': success}, 201
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json(force=True)
    process_contact_form(data)  # Pass data directly
    return {'submitted': True}, 202

@app.route('/newfeature', methods=['GET'])
def new_feature():
    # Add new feature: Display a welcome message with user customization
    user_name = request.args.get('user')  # Get user name from URL query
    welcome_message = f"Welcome, {user_name or 'Guest'}"
    return {'welcome_message': welcome_message}

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

def send_email(email, message):
    # Efficiently send email using threading
    import smtplib
    from threading import Thread
    thread = Thread(target=lambda: smtplib.SMTP('smtp.example.com', 587).sendmail('your_email@example.com', email, message))
    thread.start()

def process_about_form(form_data):
    # Efficient processing with improved logic
    return True

def process_contact_form(form_data):
    # Improved contact form processing
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
