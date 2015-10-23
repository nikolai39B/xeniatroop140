"""
FILE:
    outings_add.py
 
DIRECTORY:
    xeniatroop140/source/pages/outings

DESCRIPTION:
    This file manages requests to '/outings/add' (the add outings page).
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
contentFilename = 'outings_add.html'
pageTemplateValues = { 
    'content_title': 'Add an Outing',
    'page_title': 'Troop 140',
    'scripts': [ 'scripts/outings_add.js' ]
}

class Outings_Add(webapp2.RequestHandler):
    def get(self):
        # Determine if the user can add an outing

        contentTemplateValues = {
            'buttons_top': ou.getOutingButtonsTop(self)
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

    def post(self):
        pass

