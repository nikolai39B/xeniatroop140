"""
FILE:
    datetimeUtilities.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file contains an assortment of utility methods for related to datetimes.
"""
# Python
import datetime
import logging

#------#
# Data #
#------#
htmlDatetimeFormat = '%Y-%m-%dT%H:%M'

#---------#
# Methods #
#---------#
def htmlDatetimeToPythonDatetime(htmlDatetime):
    """
    Converts the given html datetime string to a python datetime instance.

    htmlDatetime: a string represeting the datetime in html format

    returns: datetime
    """
    return datetime.datetime.strptime(htmlDatetime, htmlDatetimeFormat)

def tryHtmlDatetimeToPythonDatetime(htmlDatetime):
    """
    Trys to convert the given html datetime string to a python datetime instance.
    Will not throw exceptions.

    htmlDatetime: a string represeting the datetime in html format

    returns: datetime (or None)
    """
    try:
        return htmlDatetimeToPythonDatetime(htmlDatetime)
    except:
        return None


def pythonDatetimeToHtmlDatetime(pythonDatetime):
    """
    Converts the given python datetime instance into an html datetime string.

    pythonDatetime: the python datetime instance

    returns: string
    """
    return pythonDatetime.strftime(htmlDatetimeFormat)


def tryPythonDatetimeToHtmlDatetime(pythonDatetime):
    """
    Trys to convert the given python datetime instance into an html datetime string.
    Will not throw exceptions.

    pythonDatetime: the python datetime instance

    returns: string
    """
    try:
        return pythonDatetimeToHtmlDatetime(pythonDatetime)
    except:
        return ''
