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

"""
In order for python to actually find our modules, we need to add their location to
the path. Every time you want to add another import, check this list and make sure
that the path to it is here.
"""
sys.path.insert(0, os.path.join(rootDir, 'source/database_models'))
#sys.path.insert(0, os.path.join(rootDir, 'source/pages'))
#sys.path.insert(0, os.path.join(rootDir, 'source/pages/login'))
#sys.path.insert(0, os.path.join(rootDir, 'source/pages/outings'))
sys.path.insert(0, os.path.join(rootDir, 'source/utilities'))

from source.pages import home
from source.pages.login import login
from source.pages.login import logout
from source.pages.outings import outings

from source.pages import notFound

app = webapp2.WSGIApplication([ 
    ('/', home.Home),
    ('/login', login.Login),
    ('/logout', logout.Logout),
    ('/outings', outings.Outings),

    ('/.*', notFound.NotFound)
], debug=True)