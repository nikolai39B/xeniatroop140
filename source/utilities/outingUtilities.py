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
import source.database_models.outing as out
import source.utilities.jinjaTemplateRenderer as jtr
import source.utilities.userAccountUtilities as uau

#------#
# Data #
#------#
pathToOutingTemplates = 'html/templates/outings'
outingTemplateName = 'outing.html'
buttonsTopTemplateName = 'outings_buttons_top.html'
outingsContainerTemplateName = 'outings_container.html'

#---------#
# Methods #
#---------#
def getRenderedOuting(outing):
    """
    Renders and returns an outing in html.

    outing: the outing whose html to generate

    returns: string
    """
    return jtr.getRenderedTemplate(pathToOutingTemplates, outingTemplateName, { 'outing': outing })

def getRenderedOutings(outings):
    """
    Renders and returns multiple outings in html.

    outings: the list of outings whose html to generate

    returns: string
    """
    outingsHtml = ''
    for outing in outings:
        outingsHtml += getRenderedOuting(outing)

    return outingsHtml

def getRenderedOutingsContainer(outings, showShowcase = True, showUpcoming = True, showPast = True):
    """
    Renders and returns the outings container with the given outings.

    outings: the list of outings whose html to generate
    showShowcase: whether to show the showcase outings
    showUpcoming: whether to show the upcoming outings
    showPast: whether to show the past outings

    returns: string
    """
    # Showcase Outings
    showcaseOutings = []
    for outing in outings:
        if outing.showcase:
            showcaseOutings.append(outing)

    showcaseOutings.sort(key=lambda o: o.departureTime, reverse=True)
    showcaseHtml = getRenderedOutings(showcaseOutings)

    # Upcoming and Past Outings
    upcomingOutings = []
    pastOutings = []
    for outing in outings:
        if outing.departureTime > datetime.datetime.now():
            upcomingOutings.append(outing)
        else:
            pastOutings.append(outing)

    upcomingOutings.sort(key=lambda o: o.departureTime)
    pastOutings.sort(key=lambda o: o.departureTime, reverse=True)
    upcomingHtml = getRenderedOutings(upcomingOutings)
    pastHtml = getRenderedOutings(pastOutings)

    # Render the container
    templateValues = {
        'show_past': showPast,
        'show_showcase': showShowcase,
        'show_upcoming': showUpcoming,
        'past_outings': pastHtml,
        'showcase_outings': showcaseHtml,
        'upcoming_outings': upcomingHtml
    }

    return jtr.getRenderedTemplate(pathToOutingTemplates, outingsContainerTemplateName, templateValues)

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

def getOutingButtonsTop(handler):
    """
    Renders and returns the buttons for the top of an outings page.

    handler: the current page handler

    returns: string
    """
    # Determine if the user can add an outing
    loggedInUser = uau.getLoggedInUser(handler)
    canAddOuting = False
    if loggedInUser != None and uau.doesUserHavePermission(loggedInUser.accountLevel, uau.poster):
        canAddOuting = True

    # Get the rendered buttons
    return jtr.getRenderedTemplate(pathToOutingTemplates, buttonsTopTemplateName, { 'can_add_outing': canAddOuting })

def createOuting(outingName, description, departureTime, returnTime, meetLocation, outingLocation, showcase, creatorId):
    """
    Creates a new outing with the given parameters.

    outingName: the name of the outing
    description: description for the outing
    departureTime: the time to depart from the outing
    returnTime: the time to return from the outing
    meetLocation: the location to meet to depart for the outing
    outingLocation: the location of the outing
    showcase: whether to showcase this outing
    creatorId: the datastore key for the outing creator

    returns: Outing
    """
    return out.Outing(
        outingName = outingName,
        description = description if description != None else '',
        departureTime = departureTime,
        returnTime = returnTime,
        meetLocation = meetLocation,
        outingLocation = outingLocation,
        showcase = showcase if showcase != None else False,
        creatorId = creatorId)

def outingParametersAreValid(outingName, description, departureTime, returnTime, meetLocation, outingLocation, showcase):
    """
    Checks the given parameters to make sure they are valid. Returns a two values:
    whether they were all correct and the error message.

    outingName: the name of the outing
    description: description for the outing
    departureTime: the time to depart from the outing
    returnTime: the time to return from the outing
    meetLocation: the location to meet to depart for the outing
    outingLocation: the location of the outing
    showcase: whether to showcase this outing

    returns: bool, string
    """
    allCorrect = True
    errorMessage = []

    # Check outing name
    if outingName == None or outingName == '':
        errorMessage.append('Outing name cannot be blank.')
        allCorrect = False

    # Check description
    if description == None:
        # Always valid
        pass

    # Check departure time
    if departureTime == None:
        errorMessage.append('Outing must have a departure time.')
        allCorrect = False
        
    # Check return time
    if returnTime == None:
        errorMessage.append('Outing must have a return time.')
        allCorrect = False

    # Check departure time before return time
    if departureTime != None and returnTime != None and departureTime > returnTime:
        errorMessage.append('Departure time must be before return time.')
        allCorrect = False

    # Check meet location
    if meetLocation == None or meetLocation == '':
        errorMessage.append('Meet location cannot be blank.')
        allCorrect = False

    # Check outing location
    if outingLocation == None or outingLocation == '':
        errorMessage.append('Outing location cannot be blank.')
        allCorrect = False

    if showcase == None:
        # Always valid
        pass

    # TODO: implement
    return allCorrect, errorMessage
