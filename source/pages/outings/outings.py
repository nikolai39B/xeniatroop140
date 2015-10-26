"""
FILE:
    outings.py
 
DIRECTORY:
    xeniatroop140/source/pages/outings

DESCRIPTION:
    This file manages requests to '/outings' (the outings page).
"""

# Python
import datetime
import logging
import os
import time

# GAE
import webapp2

# Application
import requestHandler as rh
import source.utilities.outingUtilities as ou
import source.utilities.jinjaTemplateRenderer as jtr
import source.utilities.userAccountUtilities as uau
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content/outings')
contentFilename = 'outings.html'
pageTemplateValues = { 
    'content_title': 'All Outings',
    'page_title': 'Troop 140',
    'login_redirect_link': '/outings',
    'stylesheets': [ 'stylesheets/outings/outings.css' ]
}

class Outings(webapp2.RequestHandler):
    def get(self):
        contentTemplateValues = {
            'outing_buttons_top': ou.getOutingButtonsTop(self),
            'outings': ou.getRenderedOutings(ou.getOutingInstances())
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

