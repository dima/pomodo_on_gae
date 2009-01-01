#!/usr/bin/env python

import logging
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from app.controllers import posts, comments

class AppController(webapp.RequestHandler):
  def get(self):
    self.redirect("/public/index.html")

def main():
  application = webapp.WSGIApplication(
  [('/*$', AppController), ('/posts.*', posts.Controller), ('/comments.*', comments.Controller)],
    debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
