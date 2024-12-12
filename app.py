
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return {'message': f'Name: {name}, Email: {email}, Message: {message}'}
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Process the form data here
        return {'success': True}
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data here
        return {'submitted': True}
    return render_template('contact.html')

@app.route('/success', methods=['GET'])
def success():
    return 'Form submission successful!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
