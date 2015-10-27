﻿"""
FILE:
    outings_showcase.py
 
DIRECTORY:
    xeniatroop140/source/pages/outings

DESCRIPTION:
    This file manages requests to '/outings/showcase' (the showcase outings page).
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
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content/outings')
contentFilename = 'outings.html'
pageTemplateValues = { 
    'content_title': 'Showcase Outings',
    'page_title': 'Troop 140',
    'login_redirect_link': '/outings/showcase',
    'stylesheets': [ 'stylesheets/outings/outings.css' ]
}

class Outings_Showcase(webapp2.RequestHandler):
    def get(self):
        contentTemplateValues = {
            'outing_buttons_top': ou.getOutingButtonsTop(self),
            'outings': ou.getRenderedOutingsContainer(ou.getOutingInstances(), True, False, False)
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

