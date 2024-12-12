
from flask import Flask

app = Flask(__name__)

# New feature: Contact page
@app.route('/contact', methods=['GET'])
def contact():
    return '<html><body><h2>Contact Us</h2><p>Email: contact@example.com</p></body></html>'

# Improved feature: About page with dynamic content
@app.route('/about', methods=['GET'])
def about():
    company_name = "Acme Inc."
    return '<html><body><p>Welcome to the about page of ' + company_name + '</p></body></html>'

# Efficiency: Error handling for 404 and 500 errors
@app.errorhandler(404)
def not_found(error):
    return '<html><body><h2>404 - Page Not Found</h2></body></html>', 404

@app.errorhandler(500)
def internal_error(error):
    return '<html><body><h2>500 - Internal Server Error</h2></body></html>', 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
