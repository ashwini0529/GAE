#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from google.appengine.api import users
from gaesessions import get_current_session
import pickle

userbase = {}

html  = """
	<html>
	<title>ACM GAE</title>
	<h1> Hey there.! </h1>
	<p>Hello how are you? Welcome to the app engine workshop! </p>
	<p> I hope everything is going awesome! </p>
	<p> to sign in click <a href = "/sign">here</a> </p>
	<p> Page Count : %d <p>
	</html>
"""

signInHtml = """
<html>
<body>
<form action = "/display" method = "post">
<label>Name : </label> <input type = "text" name = "username">
<label>Password : </label> <input type = "password" name = "password">
<input type = "submit">
</form>
</body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	session = get_current_session()
    	count= session.get('count' , 0)
    	session['count'] = count+1
        self.response.write(html % session['count'])
class signIn(webapp2.RequestHandler):
	def get(self):
		self.response.write(signInHtml)
class displayValues(webapp2.RequestHandler):
	def post(self):
		session = get_current_session()
		username = session.get('username' , "")
		password = session.get('password', "")
		username = cgi.escape(self.request.get('username'))
		password = cgi.escape(self.request.get('password'))
		#username = session.get('username')
		if(username) != "" and password != "":
			self.response.write('<html><body><h3>You wrote : </h3>')
			self.response.write('<h4>Username  : ')
			self.response.write(username)
			self.response.write('</h4><h4>Password  : ')	
			self.response.write(password)
			self.response.write('</h4></body></html>')
		else:
			self.response.write('Empty username or password <a href = "/">Go Back</a>')	
class userProfile(webapp2.RequestHandler):
	def get(self):
		session = get_current_session()
		if(session['username']!="" and session['password'] !=""):
			self.response.write('Welcome '+ session['username'])
			self.response.write('<br>Your Password: '+ session['password'])
		else:
			self.response.write('User not signed in!!!')	
			self.response.write('Welcome '+ session['username'])
			self.response.write('<br>Your Password: '+ session['password'])
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', signIn),
    ('/display', displayValues),
    ('/profile', userProfile)
], debug=True)