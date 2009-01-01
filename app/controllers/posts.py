# The MIT License
# 
# Copyright (c) 2008 Dima Berastau
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

__author__ = 'Dima Berastau'

import logging
import restful

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from app import models

class Controller(restful.Controller):
  def get(self):
    restful.send_successful_response(self, models.all(models.Post))
    
  @restful.methods_via_query_allowed
  def post(self, *params):
    post = models.Post()
    models.update_model_from_params(post, self.request.params)
    restful.send_successful_response(self, post.to_xml())
    
  def put(self, *params):
    post = models.Post.get(db.Key(restful.get_model_key(self)))
    models.update_model_from_params(post, self.request.params)
    restful.send_successful_response(self, post.to_xml())

  def delete(self):
    post = models.Post.get(db.Key(restful.get_model_key(self)))
    db.delete(post)
    restful.send_successful_response(self, post.to_xml())