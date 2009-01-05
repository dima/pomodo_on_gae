from google.appengine.ext import db

class ProjectCategory(db.Model):
  name = db.StringProperty()
  user = db.UserProperty()
  
  