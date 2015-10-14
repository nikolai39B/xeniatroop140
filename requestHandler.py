"""
FILE:
    requestHandler.py
 
DIRECTORY:
    xeniatroop140

DESCRIPTION:
    This file contains the app field, which maps requests to their appropriate
    handler. It also sets up the environment.
"""

# Python
import os
import sys

# GAE
import webapp2

# Application
rootDir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(rootDir, 'source/database_models'))
sys.path.insert(0, os.path.join(rootDir, 'source/pages'))
sys.path.insert(0, os.path.join(rootDir, 'source/pages/login'))
sys.path.insert(0, os.path.join(rootDir, 'source/utilities'))
import home
import login
import logout
import notFound

app = webapp2.WSGIApplication([ 
    ('/', home.Home),
    ('/login', login.Login),
    ('/logout', logout.Logout),

    ('/.*', notFound.NotFound)
], debug=True)