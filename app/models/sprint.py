from google.appengine.ext import db
import project

class Sprint(db.Model):
  name = db.StringProperty()
  due_by = db.DateTimeProperty(auto_now_add = True)
  billed_hourly_rate = db.IntegerProperty(default = 0)
  project = db.ReferenceProperty(project.Project)
  user = db.UserProperty()
