from google.appengine.ext import db
import account

class Location(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  account = db.ReferenceProperty(account.Account)
  
  