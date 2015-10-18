"""
FILE:
    userAccountUtilities.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file manages creating and verifying user accounts
    and the current logged in user.
"""

# Python
import datetime
import re
import time

# GAE
from google.appengine.ext import db

# Application
import source.database_models.userAccount as ua
import source.utilities.encryptionUtilities as enUtil

#------#
# Data #
#------#
# user cookie name
userCookieName = 'loggedInUser'

# user account levels
owner = 0
admin = 1
poster = 2
user = 3
loggedOut = 4

#---------#
# Methods # 
#---------#

def getLoggedInUser(handler):
    """
    Gets the currently logged in UserAccount. The handler is required to get the
    user cookie.

    handler: the handler to use to get the cookie

    returns: UserAccount
    """
    # Fetch and check the cookie
    cookie = handler.request.cookies.get(userCookieName)
    if cookie == None:
        return None
    currentUserUsername = enUtil.tryGetUserFromCookie(cookie)

    # If the cookie check failed, we have no logged in user
    if currentUserUsername == None:
        return None

    # If it passed, try to get the user with that username
    else:
        return getUserWithUsername(currentUserUsername)

def doesUsernameAndPasswordMatch(username, password):
    """
    Checks to see if the given password is correct for the user with
    the given username.

    username: the user to check
    password: the password to check

    returns: bool
    """
    user = getUserWithUsername(username)

    # If there is no user with this username, return False
    if user == None:
        return False

    # Check the password
    return enUtil.isHashAndSaltValidForValue(password, user.passwordHashAndSalt)

def createUserAccount(firstName, lastName, username, password, accountLevel):
    """
    Creates a new account with given parameters and creates a password hash and salt
    for the password. Does not check any parameters to ensure they are valid.

    firstName: the first name of the user
    lastName: the last name of the user
    username: the username of the user
    password: the password of the user
    accountLevel: the account level of the user

    returns: UserAccount
    """
    return ua.UserAccount(
        firstName = firstName,
        lastName = lastName,
        username = username,
        passwordHashAndSalt = enUtil.makeHashAndSaltString(password),
        accountLevel = accountLevel)

def userAccountParametersAreValid(firstName, lastName, username, password, verify, accountLevel):
    """
    Checks the given parameters to make sure they are valid. Returns a tuple containing
    whether they were all correct and the error message. Providing None for a parameter
    will skip checking that parameter.

    firstName: the first name to check
    lastName: the last name to check
    username: the username to check
    password: the password to check
    verify: the duplicated password to check
    accountLevel: the account level to check

    returns: (bool, string)
    """
    # TODO: implement
    return (True, "")

def getUserWithUsername(username):
    """
    Returns the user with the given username.

    username: the username whose user to find

    returns UserAccount (or None)
    """
    userWithUsername = db.GqlQuery("SELECT * FROM UserAccount "
                                   "WHERE username = :1 "
                                   "LIMIT 1", username)
    return userWithUsername.get()

def userWithUsernameExists(username):
    """
    Checks whether a user with the given username already exists.

    username: the username to check

    returns: bool
    """
    # If we didn't end up None, there is a user
    return getUserWithUsername(username) != None

def doesUserHavePermission(userAccountLevel, requiredAccountLevel):
    """
    Determines whether the given user account level is meets the required account level.

    userAccountLevel: the level of the given user
    requiredAccountLevel: the required level

    returns: bool
    """
    return userAccountLevel <= requiredAccountLevel

def setCookieForUser(username, handler):
    """
    Makes and sets a new cookie for the user with the given username.
    The handler that is calling this method should be passed in the second
    parameter. For most callers, this should be 'self'. The cookie will
    expire in four weeks.

    username: the user to make the cookie for
    handler: the handler to use to set the cookie
    """
    cookie = enUtil.makeCookieForValue(username)
    handler.response.set_cookie(
        userCookieName,
        cookie, 
        expires=datetime.datetime.now() + datetime.timedelta(weeks=4),
        path='/')

def deleteUserCookie(handler):
    """
    Deletes the cookie corresponding to the current user. The handler 
    that is calling this method should be passed in the second parameter.
    For most callers, this should be 'self'. 

    handler: the handler to use to delete the cookie
    """
    # To delete a cookie, set the expiration date sometime in the past
    handler.response.set_cookie(
        userCookieName,
        "",
        path = '/',
        expires = datetime.datetime.now() - datetime.timedelta(days=1))

def makeGenericOwnerAccount():
    """
    Makes a generic owner account and adds it to the database.
    FOR DEBUGGING PURPOSES ONLY. NEVER EVER CALL THIS IN DEPLOYED CODE.
    """
    newAccount = createUserAccount('Generic', 'Account', 'ga', 'ga', owner)
    newAccount.put()

    time.sleep(1);
