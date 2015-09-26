#!/usr/bin/env python

import os
import datetime
import webapp2
import logging

class TasksPage(webapp2.RequestHandler):
	def get(self):
		logging.info('TasksPage Class requested...')
		self.response.out.write('TasksPage class requested!')
		pass


app=webapp2.WSGIApplication([
	('/tasks',TasksPage)
	], debug=True)