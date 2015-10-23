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
def getQueryValues(handler, names):
    """
    Fetches the values from the elements with the given names and returns
    them in a list in the same order as names.

    handler: the current handler
    names: the names of the elements to query

    returns: list of strings
    """
    # Iterate through all the names and request the values
    values = []
    for name in names:
        values.append(handler.request.get(name))

    return values
