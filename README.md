# Gen Evolution

- Can we make an AI develop random code?

Yes.

- Can we launch it from Github Actions?

Yes.

- Can we let it commit, push, and trigger again the Actions?

yes.

## How it works

- Create a PAT key with access to this repo
- add following secretsd to this repo's secrets:
  - PAT
  - COHERE_API_KEY
  - GIT_EMAIL and GIT_USER
- Go to this repo's settings > Actions > General and allow Workflow permissions and Access.
- create a new branch and watch
- stop the last running workflow to stop

## How it's going

START:1

First app.py Flask environment

END:1