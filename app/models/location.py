from google.appengine.ext import db
import user

class Location(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  user = db.ReferenceProperty(user.User)
  
  