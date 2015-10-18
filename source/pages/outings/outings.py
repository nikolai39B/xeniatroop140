"""
FILE:
    outings.py
 
DIRECTORY:
    xeniatroop140/source/pages/outings

DESCRIPTION:
    This file manages requests to '/outings' (the outings page).
"""

# Python
import logging
import os
import sys

# GAE
import webapp2

# Application
import jinjaTemplateRenderer as jtr
import requestHandler as rh
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content/outings')
contentFilename = 'outings.html'
pageTemplateValues = { 
    'content_title': 'Outings',
    'page_title': 'Troop 140',
    #'scripts': [ 'scripts/login/outings.js' ]
}

class Outings(webapp2.RequestHandler):
    def get(self):

        contentTemplateValues = {
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

