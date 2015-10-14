"""
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
import userAccountUtilities as uau

#----------------#
# Page Rendering #
#----------------#
"""
Renders and returns page_base.html after inserting the template values. The templateValues
dictionary should contain 'page_title', 'content_title', 'content', optionally
'stylesheets', and no other values. Any additional templating to be done to 'content' should
be done before calling this method.

handler: the current page handler
templateValues: a dictionary of values for the template

returns: string
"""    
def getRenderedPage(handler, templateValues):
    # Get an environment for the html blocks
    jinjaEnv = getJinjaEnv(os.path.join(rh.rootDir, 'html/templates'))

    # Get the current user
    currentUser = uau.getLoggedInUser(handler)

    # Render the buttons_top
    tv = {
        'user': 'Guest',
        'loggedIn': False
    }
    if currentUser != None:
        tv['user'] = '%s %s' % (currentUser.firstName, currentUser.lastName)
        tv['loggedIn'] = True
    
    templateValues['buttons_top'] = getRenderedTemplateWithEnvironment(jinjaEnv, 'buttons_top.html', tv)
        
    # Render the buttons_side
    templateValues['buttons_side'] = getRenderedTemplateWithEnvironment(jinjaEnv, 'buttons_side.html')

    # Render page_base.html
    return getRenderedTemplateWithEnvironment(jinjaEnv, 'page_base.html', templateValues)

#-------------------#
# Generic Rendering #
#-------------------#
"""
Renders and returns the jinja template located at the given path with the given values.

pathToTemplate: the path to the template
templateFilename: the name of the template
templateValues: a dictionary of values for the template

returns: string
"""        
def getRenderedTemplate(pathToTemplate, templateFilename, templateValues = {}):
    # Get the environment
    jinjaEnv = getJinjaEnv(pathToTemplate)

    # Render and return the template
    return getRenderedTemplateWithEnvironment(jinjaEnv, templateFilename, templateValues)

"""
Renders and returns the jinja template located at the given path with the given values.
Use this method if you already have the jinja environment created.

jinjaEnv: the jinja environment
templateFilename: the name of the template
templateValues: a dictionary of values for the template

returns: string
"""  
def getRenderedTemplateWithEnvironment(jinjaEnv, templateFilename, templateValues = {}):
    # Get the template from the environment
    template = jinjaEnv.get_template(templateFilename)

    # Render and return the template
    return template.render(templateValues)

"""
Builds and returns the jinja environment instance for the given path.

pathToTemplate: the path for the jinja environment

returns: jinja2.Environment
"""
def getJinjaEnv(pathToTemplates):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(pathToTemplates),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

