
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(email, message)  # New feature: Send email
        return {'message': f'Name: {name}, Email: {email}, Message: {message}', 'success': True}, 200  # HTTP Status: OK
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}  # Improve form data handling
        return {'success': process_about_form(**data)}, 201

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = {key: request.form[key] for key in request.form}  # Improve form data handling
        process_contact_form(**data)
        return {'submitted': True}, 202

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
