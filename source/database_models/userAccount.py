"""
FILE:
    userAccount.py
 
DIRECTORY:
    xeniatroop140/source/database_models

DESCRIPTION:
    This file contains the database model corresponding to a user account.
"""

# GAE
from google.appengine.ext import db

class UserAccount(db.Model):
    firstName = db.StringProperty(required = True)
    lastName = db.StringProperty(required = True)
    username = db.StringProperty(required = True)
    passwordHashAndSalt = db.StringProperty(required = True)
    accountLevel = db.IntegerProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
