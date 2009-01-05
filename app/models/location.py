from google.appengine.ext import db

class Location(db.Model):
  name = db.StringProperty()
  notes = db.TextProperty()
  user = db.UserProperty()
  
  