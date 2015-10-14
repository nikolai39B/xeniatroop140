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
import encryptionUtilities as enUtil
from userAccount import UserAccount

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
"""
Gets the currently logged in UserAccount. The handler is required to get the
user cookie.

handler: the handler to use to get the cookie

returns: UserAccount
"""
def getLoggedInUser(handler):
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
        user = db.GqlQuery("SELECT * FROM UserAccount "
                           "WHERE username = :1 "
                           "LIMIT 1", currentUserUsername)
        return user.get()

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
def createUserAccount(firstName, lastName, username, password, accountLevel):
    return UserAccount(
        firstName = firstName,
        lastName = lastName,
        username = username,
        passwordHashAndSalt = enUtil.makeHashAndSaltString(password),
        accountLevel = accountLevel)

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
def userAccountParametersAreValid(firstName, lastName, username, password, verify, accountLevel):
    # TODO: implement
    return (True, "")

"""
Checks whether a user with the given username already exists.

username: the username to check

returns: bool
"""
def userWithUsernameExists(username):
    # Try to get a user with this username
    userWithUsername = db.GqlQuery("SELECT * FROM UserAccount "
                                   "WHERE username = :1 "
                                   "LIMIT 1", username)
    userWithUsername = userWithUsername.get()

    # If we didn't end up None, there is a user
    return userWithUsername != None

"""
Determines whether the given user account level is meets the required account level.

userAccountLevel: the level of the given user
requiredAccountLevel: the required level

returns: bool
"""
def doesUserHavePermission(userAccountLevel, requiredAccountLevel):
    return userAccountLevel <= requiredAccountLevel

"""
Makes and sets a new cookie for the user with the given username.
The handler that is calling this method should be passed in the second
parameter. For most callers, this should be 'self'. The cookie will
expire in four weeks.

username: the user to make the cookie for
handler: the handler to use to set the cookie
"""
def setCookieForUser(username, handler):
    cookie = enUtil.makeCookieForValue(username)
    handler.response.set_cookie(
        userCookieName,
        cookie, 
        expires=datetime.datetime.now() + datetime.timedelta(weeks=4),
        path='/')

"""
Deletes the cookie corresponding to the current user. The handler 
that is calling this method should be passed in the second parameter.
For most callers, this should be 'self'. 

handler: the handler to use to delete the cookie
"""
def deleteUserCookie(handler):
    # To delete a cookie, set the expiration date sometime in the past
    handler.response.set_cookie(
        userCookieName,
        "",
        path = '/',
        expires = datetime.datetime.now() - datetime.timedelta(days=1))

"""
Makes a generic owner account and adds it to the database.
FOR DEBUGGING PURPOSES ONLY. NEVER EVER CALL THIS IN DEPLOYED CODE.
"""
def makeGenericOwnerAccount():
    newAccount = createUserAccount('Generic', 'Account', 'ga', 'ga', owner)
    newAccount.put()

    time.sleep(1);
