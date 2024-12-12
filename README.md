# Gen Evolution

- Can we make an AI develop random code?

Yes.

- Can we launch it from Github Actions?

Yes.

- Can we let it commit, push, and trigger again the Actions?

yes.

## How it's going

START:1

First app.py Flask environment

END:1


START:2

I have updated the script by adding a new route `/greet` that greets a person by name. This feature uses the `request.args.get('name')` to retrieve the name parameter from the URL query string. If a name is provided, it returns a personalized greeting; otherwise, it prompts the user to provide a name. 

Additionally, the response format has been changed from HTML to JSON for the `/` route, returning a dictionary with a simple "Hello" and "World" greeting. 

These improvements make the script more versatile and functional, allowing for more interactive and dynamic behavior.

END:2