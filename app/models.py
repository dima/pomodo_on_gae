from google.appengine.ext import db


def update_model_from_params(model, params):
  for k, v in params.items():
    setattr(model, k, v)

  model.put()

class Post(db.Model):
  title = db.StringProperty()
  content = db.StringProperty(multiline=True)