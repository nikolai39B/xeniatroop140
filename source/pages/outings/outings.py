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
    'content_title': 'Outings',
    'page_title': 'Troop 140',
    'scripts': [ 'scripts/outings.js' ],
    'stylesheets': [ 'stylesheets/outings/outings.css' ]
}

class Outings(webapp2.RequestHandler):
    def get(self):

        # FOR DEBUGGING
        # Add some events
        """
        newOuting = ou.createOuting(
            outingName = 'Test',
            departureTime = datetime.datetime.now() - datetime.timedelta(days=3),
            returnTime = datetime.datetime.now(),
            meetLocation = 'Here',
            outingLocation = 'There',
            description = 'This is a test outing.',
            showcase = True)
        newOuting.put()

        time.sleep(1)
        """
        # END

        # Determine if the user can add an outing
        loggedInUser = uau.getLoggedInUser(self)
        canAddOuting = False
        if loggedInUser != None and uau.doesUserHavePermission(loggedInUser.accountLevel, uau.poster):
            canAddOuting = True

        contentTemplateValues = {
            'can_add_outing': canAddOuting,
            'outings': ou.getRenderedOutings(ou.getOutingInstances())
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

