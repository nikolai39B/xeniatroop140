"""
FILE:
    unauthorized.py
 
DIRECTORY:
    xeniatroop140/source/pages

DESCRIPTION:
    This file manages requests to '/unauthorized' (the unauthorized redirect page).
"""

# Python
import logging
import os
import sys

# GAE
import webapp2

# Application
import requestHandler as rh
import source.utilities.jinjaTemplateRenderer as jtr
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content')
contentFilename = 'unauthorized.html'
pageTemplateValues = { 
    'page_title': 'Troop 140',
    'content_title': 'Unauthorized',
}

class Unauthorized(webapp2.RequestHandler):
    def get(self):
        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, {}, pageTemplateValues)
