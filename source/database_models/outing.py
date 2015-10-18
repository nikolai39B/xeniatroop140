"""
FILE:
    outing.py
 
DIRECTORY:
    xeniatroop140/source/database_models

DESCRIPTION:
    This file contains the database model corresponding to a troop outing.
"""

# GAE
from google.appengine.ext import db

class Outing(db.Model):
    # Basic info
    outingName = db.StringProperty(required = True)
    description = db.StringProperty()

    # Timing
    departureTime = db.DateTimeProperty(required = True)
    returnTime = db.DateTimeProperty(required = True)

    # Location
    meetLocation = db.StringProperty(required = True)
    outingLocation = db.StringProperty(required = True)

    # Showcase
    showcase = db.BooleanProperty()
    
    # Created
    created = db.DateTimeProperty(auto_now_add = True)
