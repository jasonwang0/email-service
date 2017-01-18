import re
from validate_email import validate_email

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)


class Email():
  EMAIL_FIELDS = ["to", "from"]
  FIELDS = "to to_name from from_name subject body".split()
  def __init__(self, raw_data):
    self.populate_fields(raw_data)
    self.validate_emails()
    self.sanitize_body()

  def populate_fields(self, raw_data):
    fields = "to to_name from from_name subject body".split()
    for key in self.FIELDS:
      if raw_data.has_key(key) and isinstance(raw_data[key], basestring):
        setattr(self, key, str(raw_data[key]))
      else:
        raise Exception("Error, invalid data for '{}'.".format(key))

  def validate_emails(self):
    for field in self.EMAIL_FIELDS:
      address = getattr(self, field)
      if not validate_email(address):
        raise Exception("Error, invalid email '{}'".format(address))

  def sanitize_body(self):
    self.body = remove_tags(self.body)