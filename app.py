
from flask import Flask

app = Flask(__name__)

# New feature: Contact page with a form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if app.request.method == 'POST':
        # Process the form data here
        return 'Form submitted successfully!'
    else:
        return '''
            <html>
                <body>
                    <h1>Contact Us</h1>
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

@app.route('/')
def hello():
    return '<html><body><h1>Hello, World!</h1></body></html>'

@app.route('/about')
def about():
    return '<html><body><p>This is the about page.</p></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
