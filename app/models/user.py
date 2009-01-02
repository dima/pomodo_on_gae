from google.appengine.ext import db

class User(db.Model):
  login = db.StringProperty()
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  email = db.StringProperty()
  
  