# Build steps:
Python Dependencies:
- bottle
- validate_email
- requests

If pip or python 2.7 has not been installed:
```
sudo brew install pip || sudo apt-get install python-pip
sudo brew install python 
```
Install dependencies:
```
sudo pip install bottle requests validate_email
```

# Running locally:
Set an environment variable 'MAIL_PROVIDER' to specify mailer provider 'sendgrid' or 'mailgun'. defaults to 'sendgrid'
run `./server.py` to start the server (may need to `chmod +x server.py`)

post json requests to [http://localhost:8080/email]()


# Comments
- Mandrill no longer works after being brought out. 
- Mailgun now requires registering recipients for test accounts.
- Sendgrid was added in liu of Mandrill and is the only service that will work out of the box.
- I used Bottle because it is a simple microframework suitable for these small projects.
- If I had additional time, I could clean up the code:
    - load api tokens from env or config files
    - write some unit tests
    - do better error handling for the endpoint
    
