"""
FILE:
    handlerUtilities.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file contains an assortment of utility methods for page handlers to use.
"""
# Python
import datetime

# Application
import source.utilities.userAccountUtilities as uau

#------#
# Data #
#------#

#---------#
# Methods #
#---------#
def getQueryValue(handler, name):
    """
    Fetches and returns the value with the given query name.

    handler: the current handler
    name: the name of the element to query

    returns: string
    """
    return handler.request.get(name)

def getQueryValues(handler, names):
    """
    Fetches the values with the given query names and returns them in a list in 
    the same order as names.

    handler: the current handler
    names: the names of the elements to query

    returns: list of strings
    """
    # Iterate through all the names and request the values
    values = []
    for name in names:
        values.append(getQueryValue(handler, name))

    return values

def userIsAuthorized(handler, requiredAccountLevel):
    """    
    Determines whether the current user's account level meets the required account level.
    If the user does not, sets the redirect flags to the unauthroized page. Usually, if this
    method returns false the caller will want to immediately return.

    handler: the current page handler
    requiredAccountLevel: the required level

    returns: bool
    """
    currentUser = uau.getLoggedInUser(handler)
    userAccountLevel = uau.loggedOut    
    if currentUser != None:
        userAccountLevel = currentUser.accountLevel

    if not uau.doesUserHavePermission(userAccountLevel, requiredAccountLevel):
        handler.redirect('/unauthorized')
        return False

    return True
