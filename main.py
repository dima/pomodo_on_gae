#!/usr/bin/env python

import logging
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from app.controllers import locations, notes, projects, restful, tasks, users

class AppController(webapp.RequestHandler):
  def get(self):
    self.redirect("/public/index.html")

def main():
  application = webapp.WSGIApplication(
  [('/*$', AppController), 
  ('/locations.*', locations.Controller),
  ('/notes.*', notes.Controller),
  ('/projects.*', projects.Controller),
  ('/restful.*', restful.Controller),
  ('/tasks.*', tasks.Controller),
  ('/users.*', users.Controller)
  ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
