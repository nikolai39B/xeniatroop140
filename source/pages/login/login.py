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
import urllib

# GAE
import webapp2

# Application
import requestHandler as rh
import source.utilities.handlerUtilities as hu
import source.utilities.jinjaTemplateRenderer as jtr
import source.utilities.userAccountUtilities as uau
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content/login')
contentFilename = 'login.html'
pageTemplateValues = { 
    'content_title': 'Login',
    'page_title': 'Troop 140',
}

# Query Keys
redirectQueryKey = 'q_redirect'

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
        username, password = hu.getQueryValues(
            self,
            [ 'i_username',
              'i_password' ])

        # Check the username and password
        success = uau.doesUsernameAndPasswordMatch(username, password)

        # If they were correct, log in
        if success:
            uau.setCookieForUser(username, self)

            # Get the redirect page if possible
            redirectPage = '/'
            redirectQueryValue = hu.getQueryValue(self, redirectQueryKey)
            if redirectQueryValue != None and redirectQueryValue != "":
                redirectPage = urllib.unquote(redirectQueryValue)

            self.redirect(redirectPage)
            
        # Otherwise, let the user know that there was an error
        else:
            contentTemplateValues = {
                'error_message': jtr.getRenderedErrorMessage('Invalid username or password.'),
                'password': '',
                'username': username
            }

            jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

