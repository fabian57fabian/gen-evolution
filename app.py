
from flask import Flask

app = Flask(__name__)

# New feature: Contact page
@app.route('/contact')
def contact():
    return '<html><body><h1>Contact Us</h1><p>Contact details: info@example.com</p></body></html>'

@app.route('/')
def hello():
    return '<html><body><h1>Hello, World!</h1></body></html>'

@app.route('/about')
def about():
    return '<html><body><p>This is the about page.</p></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
