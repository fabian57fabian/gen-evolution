
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
        data = request.get_json(force=True)  # Force JSON parsing
        success = process_about_form(**data)
        return {'success': success}, 201
    return render_template('about.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json(force=True)  # Force JSON parsing
    process_contact_form(**data)
    return {'submitted': True}, 202

@app.route('/newfeature', methods=['GET'])
def new_feature():
    return render_template('newfeature.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

def send_email(email, message):
    import smtplib
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    server.sendmail('your_email@example.com', email, message)
    server.quit()

def process_about_form(form_data):
    # Efficient processing
    return True

def process_contact_form(form_data):
    # Process contact form data
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
