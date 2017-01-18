import requests

# could break these out into their own files
def mailgun(email):
  return requests.post(
    "https://api.mailgun.net/v3/sandbox36e7aba7ad034af2905798e78ed00603.mailgun.org/messages",
    auth=("api", "key-b76f200e4981e1b45308e8a1bd96b9d3"),
    data={"from": "{0} <{1}>".format(email.from_name, getattr(email, 'from')),
          "to": [email.to],
          "subject": email.subject,
          "text": email.body})

def sendgrid(email):
  headers = {
    'Authorization': 'Bearer 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',
    'User-Agent': 'sendgrid/3;python',
    'Accept': 'application/json'
  }
  data = {
    'subject': email.subject,
    'content': [{
      'value': email.body,
      'type': "text/plain"
    }],
    'from': {
      'email': getattr(email, 'from'),
      'name': email.from_name
    },
    "personalizations": [
      {"to": [{
        "email": email.to,
        "name": email.to_name
      }]}
    ],
  }
  return requests.post(
    "https://api.sendgrid.com/v3/mail/send",
    headers=headers,
    json=data
  )

DEFAULT_SERVICE = sendgrid
SERVICE_OPTIONS = {
  'mailgun': mailgun,
  'sendgrid': sendgrid
}

class Sender():
  def __init__(self, service):
    self.service = SERVICE_OPTIONS.get(service, DEFAULT_SERVICE)

  def send(self, email):
    self.service(email)


