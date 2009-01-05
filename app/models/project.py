from google.appengine.ext import db

class Project(db.Expando):
  name = db.StringProperty()
  notes = db.TextProperty()
  start_date = db.DateProperty(auto_now_add = True)
  end_date = db.DateProperty(auto_now_add = True)
  completed = db.BooleanProperty(default = False)
  user = db.UserProperty()
  
  