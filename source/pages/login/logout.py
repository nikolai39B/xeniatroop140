"""
FILE:
    home.py
 
DIRECTORY:
    xeniatroop140/source/pages/logout

DESCRIPTION:
    This file manages requests to '/logout' (the logout page).
"""

# Python
import logging
import os
import sys

# GAE
import webapp2

# Application
import source.utilities.userAccountUtilities as uau
	
# Page Template
# Note: this page has no content; it always redirects to '/'.

class Logout(webapp2.RequestHandler):
    def get(self):
        uau.deleteUserCookie(self)
        self.redirect('/')

