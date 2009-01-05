import restful
import logging

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from app import authorized

class Controller(restful.Controller):    
  @restful.methods_via_query_allowed
  def post(self):
    pass

  def delete(self):
    restful.send_successful_response(self, "<logout>%s</logout>" % (users.create_logout_url("/"), ))
    
