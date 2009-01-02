from google.appengine.ext import db
import user

class Note(db.Model):
  content = db.TextProperty()
  user = db.ReferenceProperty(user.User)
  
  