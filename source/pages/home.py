"""
FILE:
    home.py
 
DIRECTORY:
    xeniatroop140/source/pages

DESCRIPTION:
    This file manages requests to '/' (the home page).
"""

# Python
import logging
import os
import sys

# GAE
import jinja2
import webapp2

# Application
import jinjaTemplateRenderer as jtr
import requestHandler as rh
import userAccountUtilities as uau
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content')
contentFilename = 'home.html'

class Home(webapp2.RequestHandler):
    def get(self):
        # Get the rendered page content
        content = jtr.getRenderedTemplate(pathToContent, contentFilename)

        # Set the values for the page template
        templateValues = { 
            'page_title': 'Troop 140',
            'content_title': 'Our Troop',
            'content': content,
        }

        # TEMPORARY FOR DEBUGGING. REMOVE BEFORE DEPLOYMENT
        if not uau.userWithUsernameExists('ga'):
            uau.makeGenericOwnerAccount()
        uau.setCookieForUser('ga', self)
        #uau.deleteUserCookie(self)

        # Render the page
        self.response.write(jtr.getRenderedPage(templateValues))
