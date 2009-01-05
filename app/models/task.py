from google.appengine.ext import db
import sprint

class Task(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  sprint = db.ReferenceProperty(sprint.Sprint)
  billed_percentage = db.IntegerProperty(default = 0)
  user = db.UserProperty()
  
  