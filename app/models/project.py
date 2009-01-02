from google.appengine.ext import db
import user

class Project(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  start_date = db.DateProperty()
  end_date = db.DateProperty()
  completed = db.BooleanProperty()
  user = db.ReferenceProperty(user.User)
  
  