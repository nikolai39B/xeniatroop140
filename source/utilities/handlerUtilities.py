"""
FILE:
    handlerUtilities.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file contains an assortment of utility methods for
    page handlers to use
"""

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
