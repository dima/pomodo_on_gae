from google.appengine.ext import db

class Address(db.Model):
  line_one = db.StringProperty()
  line_two = db.TextProperty()
  city = db.StringProperty()
  province = db.StringProperty()
  counry = db.StringProperty()
  postcode = db.StringProperty()
  user = db.UserProperty()
  
  