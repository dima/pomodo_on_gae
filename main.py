#!/usr/bin/env python

import logging
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from app.controllers import sessions, addresses, project_categories, projects, sprints, tasks, stats, workunits

class AppController(webapp.RequestHandler):
  def get(self):
    if users.get_current_user():
      self.redirect("/public/index.html")
    else:
      self.redirect(users.create_login_url(self.request.uri))

def main():
  application = webapp.WSGIApplication(
  [('/*$', AppController),
  ('/sessions.*', sessions.Controller),
  ('/addresses.*', addresses.Controller),
  ('/project_categories.*', project_categories.Controller),
  ('/projects.*', projects.Controller),
  ('/sprints.*', sprints.Controller),
  ('/stats.*', stats.Controller),
  ('/tasks.*', tasks.Controller),
  ('/workunits.*', workunits.Controller)
  ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
