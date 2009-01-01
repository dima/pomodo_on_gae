import logging
import restful

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from app import models

# 1. extract XML marshalling for arrays + content-type to it's own method

class Controller(restful.Controller):
  def get(self):
    self.response.headers["Content-Type"] = "application/xml"
    self.response.out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    self.response.out.write('<entities kind="Post" type="array">\n')
    for post in models.Post.all():
      self.response.out.write(post.to_xml())
    self.response.out.write('</entities>')
    
  @restful.methods_via_query_allowed
  def post(self, *params):
    post = models.Post()
    models.update_model_from_params(post, self.request.params)
    restful.send_successful_response(self, post.to_xml())
    
  def put(self, *params):
    key = self.request.path_info.split("/").pop().replace(".fxml", "")
    post = models.Post.get(db.Key(restful.get_model_key(self)))
    models.update_model_from_params(post, self.request.params)
    restful.send_successful_response(self, post.to_xml())

  def delete(self):
    post = models.Post.get(db.Key(restful.get_model_key(self)))
    db.delete(post)
    restful.send_successful_response(self, post.to_xml())