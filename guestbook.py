import cgi
from google.appengine.api import users
import webapp2

MAIN_PAGE_HTML = """\

<html>
<body>
	<form action="/sign" method = "POST">
	<input type = "text" name = "content">
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
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)