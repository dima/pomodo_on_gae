from google.appengine.ext import db
import project, location

class Task(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  start_time = db.DateTimeProperty(auto_now_add = True)
  end_time = db.DateTimeProperty(auto_now_add = True)
  completed = db.BooleanProperty(default = False)
  next_action = db.BooleanProperty(default = False)
  project = db.ReferenceProperty(project.Project)
  location = db.ReferenceProperty(location.Location)
  user = db.UserProperty()
  
  