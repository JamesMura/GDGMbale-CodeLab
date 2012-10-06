#!/usr/bin/env python
from google.appengine.ext.webapp import template
import webapp2
import os
from google.appengine.api import users
from google.appengine.api import mail
class GDGRequestHandler(webapp2.RequestHandler):
	def render(self, name, **data):
		if not data:
			data = {}
		path = os.path.join(os.path.dirname(__file__), 'templates/')
		self.response.out.write(template.render(path+name+".html", data))
class MainHandler(GDGRequestHandler):
    def get(self):
        sendEmail()
        self.render('index',user= users.get_current_user())
def sendEmail():
    user = users.get_current_user()
    message = mail.EmailMessage(sender="<jam.mura@gmail.com>",subject="Welcome to Our GDG App",to="<%s>" % user.email())
    message.body = """
    Dear %s:

    You have succesfully logged into the GDG Mbale appengine app 
    go to https://developers.google.com/appengine/ to learn more about appengine
    
    
    the code for this app can be downloaded at https://github.com/JamesMura/GDGMbale-CodeLab/zipball/master
    
    if you have any questions and need help contact me on
    https://twitter.com/murangajames

    James Muranga
    """ % user.nickname()

    message.send()
    
app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
