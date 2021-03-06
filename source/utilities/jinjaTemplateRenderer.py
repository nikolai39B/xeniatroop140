﻿"""
FILE:
    jinjaTemplateRenderer.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file contains common utility functions to help handlers render their pages and content.
    It includes a method getRenderedPage() which automatically applies titles and content to 
    the page_base.html template as well as other related utilities.
"""

# Python
import logging
import os
import sys

# GAE
import jinja2

# Application
import requestHandler as rh
import source.utilities.userAccountUtilities as uau

#------#
# Data #
#------#
pathToErrorMessageTemplate = 'html/templates'
errorMessageTemplateFilename = 'error_message.html'

#---------#
# Methods #
#---------#

    #----------------#
    # Page Rendering #
    #----------------#
def renderContentAndPage(handler, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues):
    """
    Renders the content and page with their respective template values, then writes the
    page using the handler. The contentTemplateValues dictionary contains the template values for the
    page's content, and the pageTemplateValues dictionary contains the additional template values for
    page_base.html. The pageTemplateValues dictionary should contain 'page_title', 'content_title', and
    optionally 'login_redirect_link', 'scripts' and 'stylesheets'.

    handler: the current page handler
    pathToContent: the path to the content template
    contentFilename: the content template filename
    contentTemplateValues: the template values for the content
    pageTemplateValues: the template values for the page

    returns: None
    """
    # Render the content with its template values
    content = getRenderedTemplate(pathToContent, contentFilename, contentTemplateValues)

    # Render the page with its template values
    pageTemplateValues['content'] = content
    page = getRenderedPage(handler, pageTemplateValues)

    # Write the page
    handler.response.write(page)

def getRenderedPage(handler, templateValues):
    """
    Renders and returns page_base.html after inserting the template values. The templateValues
    dictionary should contain 'page_title', 'content_title', 'content', optionally
    'login_redirect_link', 'scripts' and 'stylesheets', and no other values. Any additional templating
    to be done to 'content' should be done before calling this method.

    handler: the current page handler
    templateValues: a dictionary of values for the template

    returns: string
    """
    # Get an environment for the html blocks
    jinjaEnv = getJinjaEnv(os.path.join(rh.rootDir, 'html/templates'))

    # Get the current user
    currentUser = uau.getLoggedInUser(handler)

    # Render the buttons_top
    tempVals = {
        'user': 'Guest',
        'logged_in': False
    }

    if 'login_redirect_link' in templateValues.keys():
        # Get the login redirect link if possible
        tempVals['login_redirect_link'] = templateValues['login_redirect_link']
        
    if currentUser != None:
        # Get the user information if possible
        tempVals['user'] = '%s %s' % (currentUser.firstName, currentUser.lastName)
        tempVals['logged_in'] = True
    
    templateValues['buttons_top'] = getRenderedTemplateWithEnvironment(jinjaEnv, 'buttons_top.html', tempVals)
        
    # Render the buttons_side
    templateValues['buttons_side'] = getRenderedTemplateWithEnvironment(jinjaEnv, 'buttons_side.html')

    # Render page_base.html
    return getRenderedTemplateWithEnvironment(jinjaEnv, 'page_base.html', templateValues)

    #-------------------#
    # Generic Rendering #
    #-------------------#     
def getRenderedTemplate(pathToTemplate, templateFilename, templateValues):
    """
    Renders and returns the jinja template located at the given path with the given values.

    pathToTemplate: the path to the template
    templateFilename: the name of the template
    templateValues: a dictionary of values for the template

    returns: string
    """   
    # Get the environment
    jinjaEnv = getJinjaEnv(pathToTemplate)

    # Render and return the template
    return getRenderedTemplateWithEnvironment(jinjaEnv, templateFilename, templateValues)

def getRenderedTemplateWithEnvironment(jinjaEnv, templateFilename, templateValues = {}):
    """
    Renders and returns the jinja template located at the given path with the given values.
    Use this method if you already have the jinja environment created.

    jinjaEnv: the jinja environment
    templateFilename: the name of the template
    templateValues: a dictionary of values for the template

    returns: string
    """  
    # Get the template from the environment
    template = jinjaEnv.get_template(templateFilename)

    # Render and return the template
    return template.render(templateValues)

def getJinjaEnv(pathToTemplates):
    """
    Builds and returns the jinja environment instance for the given path.

    pathToTemplate: the path for the jinja environment

    returns: jinja2.Environment
    """
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(pathToTemplates),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

    #-----------------------------#
    # Specific Template Rendering #
    #-----------------------------#
def getRenderedErrorMessage(errorMessage):
    """
    Gets the error message template rendered with the given message.

    errorMessage: the string or list of strings to use as the error message

    returns: string
    """
    templateValues = { 'error_message': errorMessage }
    return getRenderedTemplate(pathToErrorMessageTemplate, errorMessageTemplateFilename, templateValues)
