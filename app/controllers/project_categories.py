import restful
import logging

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from app import authorized
from app.models import assist, project_category

class Controller(restful.Controller):
  @authorized.role("user")
  def get(self):
    restful.send_successful_response(self, assist.all(project_category.ProjectCategory))
    
  @restful.methods_via_query_allowed
  def post(self):
    model = project_category.ProjectCategory()
    assist.update_model_from_params(model, self.request.params)
    restful.send_successful_response(self, model.to_xml())
    
  def put(self):
    model = project_category.ProjectCategory.get_or_insert(db.Key(restful.get_model_key(self)))
    assist.update_model_from_params(model, self.request.params)
    restful.send_successful_response(self, model.to_xml())
    
  def delete(self):
    model = project_category.ProjectCategory.get(db.Key(restful.get_model_key(self)))
    db.delete(model)
    restful.send_successful_response(self, model.to_xml())
