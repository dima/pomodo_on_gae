#!/usr/bin/env python

import logging
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


class Post(db.Model):
  title = db.StringProperty()
  content = db.StringProperty(multiline=True)
  
class PostController(webapp.RequestHandler):
  def get(self):
    self.response.headers["Content-Type"] = "application/xml"
    self.response.out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    self.response.out.write('<entities kind="Post" type="array">\n')
    for post in Post.all():
      self.response.out.write(post.to_xml())
    self.response.out.write('</entities>')
    
  def post(self):
    post = Post()
    post.title = self.request.get('title')
    post.content = self.request.get('content')
    
    # This doesn't work on db.Model types, why?
    # for k, v in self.request.params.items():
    #   post[k] = v

    post.put()
    self.response.headers["Content-Type"] = "application/xml"
    self.response.out.write('<?xml version="1.0" encoding="UTF-8"?>')
    self.response.out.write(post.to_xml())
    
  def delete(self):
    db.delete(Post.all())

class AppController(webapp.RequestHandler):
  def get(self):
    self.redirect("/public/index.html")

def main():
  application = webapp.WSGIApplication(
  [('/', AppController), ('/posts.*', PostController)],
    debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
