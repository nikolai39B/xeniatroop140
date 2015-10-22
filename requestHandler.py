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
rootDir = os.path.dirname(__file__) # Be sure to do this before the below imports

from source.pages import home
from source.pages.login import login
from source.pages.login import logout
from source.pages.outings import outings
from source.pages.outings import outings_add

from source.pages import notFound

#------#
# Data #
#------#
app = webapp2.WSGIApplication([ 
    ('/', home.Home),
    ('/login', login.Login),
    ('/logout', logout.Logout),
    ('/outings', outings.Outings),
    ('/outings/add', outings_add.Outings_Add),

    ('/.*', notFound.NotFound)
], debug=True)