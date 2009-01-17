import restful
import logging

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from app import authorized
from app.models import assist, workunit

class Controller(restful.Controller):
  @authorized.role("user")
  def get(self):
    restful.send_successful_response(self, assist.all(workunit.Workunit))
    
  @restful.methods_via_query_allowed
  def post(self):
    model = workunit.Workunit()
    assist.update_model_from_params(model, self.request.params)
    restful.send_successful_response(self, model.to_xml())
    
  def put(self):
    model = workunit.Workunit.get_or_insert(db.Key(restful.get_model_key(self)))
    assist.update_model_from_params(model, self.request.params)
    restful.send_successful_response(self, model.to_xml())
    
  def delete(self):
    model = workunit.Workunit.get(db.Key(restful.get_model_key(self)))
    db.delete(model)
    restful.send_successful_response(self, model.to_xml())
