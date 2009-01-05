from google.appengine.ext import db

class Note(db.Model):
  content = db.TextProperty()
  user = db.UserProperty()
  