"""
FILE:
    outingUtilities.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file manages creating and rendering troop outings.
"""

# Python
import datetime
import re
import time

# GAE
from google.appengine.ext import db

# Application
import source.database_models.outing as outing

def createOuting(outingName, departureTime, returnTime, meetLocation, outingLocation, description = '', showcase = False):
    """
    Creates a new outing with given parameters. Does not check any parameters to 
    ensure they are valid.

    outingName: the name of the outing
    departureTime: the time to leave the meet location
    returnTime: the time everyone should be back
    meetLocation: the location everyone should initially meet
    outingLocation: the location of the outing
    description: a description of the outing
    showcase: whether to showcase this event

    returns: Outing
    """
    return outing.Outing(
        outingName = outingName,
        description = description,
        departureTime = departureTime,
        returnTime = returnTime,
        meetLocation = meetLocation,
        outingLocation = outingLocation,
        showcase = showcase)
