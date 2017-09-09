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
import frontend
import cgi


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(frontend.menu)

class SignInHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(frontend.displayForm)
	def post(self):
		name = cgi.escape(self.request.get('name'))
		self.response.write("Your name is : " + name)

class CalculatorHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(frontend.calculatorForm)
	def post(self):
		num1 = int(cgi.escape(self.request.get('num1')))
		num2 = int(cgi.escape(self.request.get('num2')))
		operation = cgi.escape(self.request.get('operation'))
		if(operation=="+"):
			self.response.write("Addition is: "+str(num1+num2))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/display', SignInHandler),
    ('/calculate', CalculatorHandler)
], debug=True)
