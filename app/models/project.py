from google.appengine.ext import db
import user

class Project(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  start_date = db.DateProperty(auto_now_add = True)
  end_date = db.DateProperty(auto_now_add = True)
  completed = db.BooleanProperty(default = False)
  user = db.ReferenceProperty(user.User)
  
  