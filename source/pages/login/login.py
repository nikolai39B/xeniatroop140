"""
FILE:
    home.py
 
DIRECTORY:
    xeniatroop140/source/pages/login

DESCRIPTION:
    This file manages requests to '/login' (the login page).
"""

# Python
import logging
import os
import sys

# GAE
import webapp2

# Application
import handlerUtilities as hr
import jinjaTemplateRenderer as jtr
import requestHandler as rh
import userAccountUtilities as uau
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content/login')
contentFilename = 'login.html'
pageTemplateValues = { 
    'content_title': 'Login',
    'page_title': 'Troop 140',
    'scripts': [ 'scripts/login/login.js' ]
}

class Login(webapp2.RequestHandler):
    def get(self):

        # TEMPORARY FOR DEBUGGING. REMOVE BEFORE DEPLOYMENT
        if not uau.userWithUsernameExists('ga'):
            uau.makeGenericOwnerAccount()

        contentTemplateValues = {
            'password': '',
            'username': ''
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

    def post(self):
        # Get the posted values
        username, password = hr.getTagValues(
            self,
            [ 'i_username',
              'i_password' ])

        # Check the username and password
        success = uau.doesUsernameAndPasswordMatch(username, password)

        # If they were correct, log in
        if success:
            uau.setCookieForUser(username, self)
            
        # Otherwise, let the user know that there was an error
        else:
            contentTemplateValues = {
                'error_message': 'Invalid username or password.',
                'password': '',
                'username': username
            }

            jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

