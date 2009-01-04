from google.appengine.ext import db
import account

class Note(db.Model):
  content = db.TextProperty()
  account = db.ReferenceProperty(account.Account)
  
  