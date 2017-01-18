#!/usr/bin/env python
import os
from bottle import Bottle, run, request

from lib.email import Email
from lib.sender import Sender

def build_app():
  app = Bottle()

  @app.post('/email')
  def email():
    try:
      raw_data = request.json
      email = Email(raw_data)
      response = mailer.send(email)
    except:
      raise

  return app

if __name__ == '__main__':
  mailer = Sender(os.environ.get('MAIL_PROVIDER'))
  app = build_app()
  run(app, host='localhost', port=8080)

