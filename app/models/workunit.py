from google.appengine.ext import db
import task

class Workunit(db.Model):
  started_on = db.DateTimeProperty(auto_now_add = True)
  ended_on = db.DateTimeProperty(auto_now_add = True)
  worked_milliseconds = db.IntegerProperty(default = 0)
  task = db.ReferenceProperty(task.Task)
  user = db.UserProperty()
