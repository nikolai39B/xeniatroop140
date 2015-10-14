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
import jinjaTemplateRenderer as jtr
import requestHandler as rh
import userAccountUtilities as uau
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content/login')
contentFilename = 'login.html'

class Login(webapp2.RequestHandler):
    def get(self):

        # TEMPORARY FOR DEBUGGING. REMOVE BEFORE DEPLOYMENT
        if not uau.userWithUsernameExists('ga'):
            uau.makeGenericOwnerAccount()
        uau.setCookieForUser('ga', self)
        #uau.deleteUserCookie(self)

        # Render the page
        pageTemplateValues = { 
            'content_title': 'Login',
            'page_title': 'Troop 140',
            'scripts': [ 'scripts/login/login.js' ]
        }
        jtr.renderContentAndPage(self, pathToContent, contentFilename, {}, pageTemplateValues)
