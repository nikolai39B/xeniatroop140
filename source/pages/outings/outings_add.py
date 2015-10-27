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
import source.utilities.datetimeUtilities as du
import source.utilities.handlerUtilities as hu
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
        # Ensuer the user can add an outing
        if not hu.userIsAuthorized(self, uau.poster):
            return

        contentTemplateValues = {
            'outings_buttons_top': ou.getOutingButtonsTop(self)
        }

        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)

    def post(self):
        # Ensuer the user can add an outing
        if not hu.userIsAuthorized(self, uau.poster):
            return

        # Get the data
        outingName, description, departureTime, returnTime, meetLocation, outingLocation, showcase = hu.getQueryValues(
            self,
            [ 'i_outing_name',
              'ta_description',
              'i_departure_time',
              'i_return_time',
              'i_meet_location',
              'i_outing_location',
              'i_showcase' ])

        departureTime = du.tryHtmlDatetimeToPythonDatetime(departureTime)
        returnTime = du.tryHtmlDatetimeToPythonDatetime(returnTime)
        showcase = True if showcase == 'True' else False

        valid, errorMessage = ou.outingParametersAreValid(outingName, description, departureTime, returnTime, meetLocation, outingLocation, showcase)

        # If all parameters are valid, then create and store the outing
        if valid:
            creatorId = ''
            try:
                uau.getLoggedInUser(self).key().id()
            except:
                logging.info('Warning: could not determine logged in user when creating outing.')

            newOuting = ou.createOuting(outingName, description, departureTime, returnTime, meetLocation, outingLocation, showcase, creatorId)
            newOuting.put()

            time.sleep(0.25)
            self.redirect('/outings')
            return

        # Otherwise, tell the user what the errors are
        else:    
            departureTime = du.tryPythonDatetimeToHtmlDatetime(departureTime)
            returnTime = du.tryPythonDatetimeToHtmlDatetime(returnTime)

            contentTemplateValues = {
                'outings_buttons_top': ou.getOutingButtonsTop(self),
                'outing_name': outingName,
                'description': description,
                'departure_time': departureTime,
                'error_message': jtr.getRenderedErrorMessage(errorMessage),
                'meet_location': meetLocation,
                'outing_location': outingLocation,
                'return_time': returnTime,
                'showcase': showcase
            }

            # Render the page
            jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)
