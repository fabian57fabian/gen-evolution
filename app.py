
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f'Name: {name}, Email: {email}, Message: {message}'
    return '''
        <html>
            <body>
                <h1>Home Page</h1>
                <form method="POST">
                    <label for="name">Name:</label><br>
                    <input type="text" id="name" name="name"><br>
                    <label for="email">Email:</label><br>
                    <input type="email" id="email" name="email"><br>
                    <label for="message">Message:</label><br>
                    <textarea id="message" name="message"></textarea><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    '''

@app.route('/about', methods=['GET', 'POST'])
def about_page():
    if request.method == 'POST':
        # Process the form data here
        return 'Form submitted on the About page!'
    return '<html><body><p>This is the about page.</p></body></html>'

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        # Process the form data here
        return 'Contact form submitted!'
    return '''
        <html>
            <body>
                <h1>Contact Us</h1>
                <form method="POST">
                    <label for="name">Name:</label><br>
                    <input type="text" id="name" name="name"><br>
                    <label for="email">Email:</label><br>
                    <input type="email" id="email" name="email"><br>
                    <label for="subject">Subject:</label><br>
                    <input type="text" id="subject" name="subject"><br>
                    <label for="message">Message:</label><br>
                    <textarea id="message" name="message"></textarea><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
