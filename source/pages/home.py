"""
FILE:
    home.py
 
DIRECTORY:
    xeniatroop140/source/pages

DESCRIPTION:
    This file manages requests to '/' (the home page).
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
import userAccountUtilities as uau
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content')
contentFilename = 'home.html'
pageTemplateValues = { 
    'page_title': 'Troop 140',
    'content_title': 'Our Troop',
}

class Home(webapp2.RequestHandler):
    def get(self):
        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, {}, pageTemplateValues)
