from google.appengine.ext import db

class Post(db.Model):
  title = db.StringProperty()
  content = db.StringProperty(multiline=True)