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
import logging
import re
import time

# GAE
from google.appengine.ext import db

# Application
import source.database_models.outing as outing
import source.utilities.jinjaTemplateRenderer as jtr

#------#
# Data #
#------#
pathToOutingTemplate = 'html/templates'
outingTemplateName = 'outing.html'

#---------#
# Methods #
#---------#
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

def getRenderedOuting(outing):
    """
    Renders and returns an outing in html.

    outing: the outing whose html to generate

    returns: string
    """
    return jtr.getRenderedTemplate(pathToOutingTemplate, outingTemplateName, { 'outing': outing })

def getRenderedOutings(outings):
    """
    Renders and returns multiple outings in html.

    outings: the list of outings whose html to generate

    returns: string
    """
    outingsHtml = ""
    for outing in outings:
        outingsHtml += getRenderedOuting(outing)

    return outingsHtml

def getOutingInstances(condition = ""):
    """
    Returns all Outing instances in the database that meet the given gql condition.

    condition: the gql string to filter instances (or empty string for no condition)

    returns: list of outings
    """
    gqlOutings = db.GqlQuery("SELECT * from Outing " + condition + " ")
    outings = []
    
    # Turn the gql object into a list
    for gqlOuting in gqlOutings:
        outings.append(gqlOuting)

    logging.info(outings)
    return outings
