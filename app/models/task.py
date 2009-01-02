from google.appengine.ext import db
import project, location, user

class Task(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  start_time = db.DateTimeProperty()
  end_time = db.DateTimeProperty()
  completed = db.BooleanProperty()
  next_action = db.BooleanProperty()
  project = db.ReferenceProperty(project.Project)
  location = db.ReferenceProperty(location.Location)
  user = db.ReferenceProperty(user.User)
  
  