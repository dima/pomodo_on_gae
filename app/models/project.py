from google.appengine.ext import db
import account

class Project(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  start_date = db.DateProperty(auto_now_add = True)
  end_date = db.DateProperty(auto_now_add = True)
  completed = db.BooleanProperty(default = False)
  account = db.ReferenceProperty(account.Account)
  
  