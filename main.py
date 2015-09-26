import cgi
from google.appengine.api import users
import webapp2
from webapp2_extras import json
import json


############################################
#Open JSON
with open('a.json') as json_file:
	string = json.loads(json_file)

#string = """{"name" : "Ashwini",
#				"email" : "ashwinipurohit@yahoo.in"}"""

############################################
MAIN_PAGE_HTML = """\

<html>
<body>
	<form action="/sign" method = "POST">
	<input type = "text" name = "name">
	<input type = "text" name = "registrationNumber" >
	<input type = "submit">
	</form>
</body>
</html>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write('NAME :')
        self.response.write(cgi.escape(self.request.get('name')))
        self.response.write('<br>') #
        self.response.write('REGISTRATION NUMBER :')
        self.response.write(cgi.escape(self.request.get('registrationNumber')))
        self.response.write('</pre></body></html>')
		
class returnJSON(webapp2.RequestHandler):
    def get(self):
    	structured_dictionary = string#json.dumps(string)
    	self.response.write(structured_dictionary)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/view', returnJSON),
], debug=True)