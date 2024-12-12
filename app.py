
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # New feature: Send an email to the specified address
        send_email(email, message)
        return {'message': f'Name: {name}, Email: {email}, Message: {message}', 'success': True}
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Process the form data here
        return {'success': process_about_form(request.form)}, 201  # HTTP Status: Created
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data here
        process_contact_form(request.form)
        return {'submitted': True}, 202  # HTTP Status: Accepted
    return render_template('contact.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')  # Use a template for better flexibility

def send_email(email, message):
    import smtplib
    server = smtplib.SMTP('smtp.example.com', 587)  # Use your SMTP server details
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    server.sendmail('your_email@example.com', email, message)
    server.quit()

def process_about_form(form):
    # Process the about form data efficiently
    # Return True if successful, False otherwise
    return True

def process_contact_form(form):
    # Process the contact form data
    # Perform necessary actions
   return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
