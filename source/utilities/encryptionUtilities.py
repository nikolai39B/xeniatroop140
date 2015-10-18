"""
FILE:
    encryptionUtilities.py
 
DIRECTORY:
    xeniatroop140/source/utilities

DESCRIPTION:
    This file manages encrypting user info into hashes. 
"""

# Python
import random
import string

# Application
import source.utilities.hashSecret as hs

#------#
# Data #
#------#
# hash/salt info
saltLength = 32
hashAndSaltTemplate = '%s|%s' # hash|salt
numHashAndSaltItems = 2

# cookie info
cookieTemplate = '%s|%s|%s' # username|hash of username|salt
numCookieItems = 3

#---------#
# Methods #
#---------#
def tryGetUserFromCookie(cookie):
    """
    Returns the username from the cookie if the cookie is valid, or None if the cookie
    is invalid.

    cookie: the cookie to attempt to get the user from

    returns string (or None)
    """
    # Make sure we have the right number of items
    items = cookie.split('|')
    if len(items) != numCookieItems:
        return None

    # Get the values
    username = items[0]
    hash = items[1]
    salt = items[2]

    # Check the hash and salt
    hashAndSalt = hashAndSaltTemplate % (hash, salt)
    if isHashAndSaltValidForValue(username, hashAndSalt):
        return username
    else:
        return None

def isHashAndSaltValidForValue(value, hashAndSalt):
    """
    Checks the given value against the hash and salt. Will throw a ValueError if
    the hashAndSalt string is not in the correct form.

    value: the value to check
    hashAndSalt: the hash and salt to check the value against

    returns: bool
    """
    # Make sure we have the right number of items
    items = hashAndSalt.split('|')
    if len(items) != numHashAndSaltItems:
        raise ValueError('Error: hash and salt did not have the correct form.')

    # Throw an exception if the salt does not have the correct length
    salt = items[1]
    if len(salt) != saltLength:
        raise ValueError('Error: salt must be of length %s. Provided salt length was %s' % (saltLength, len(salt)))

    # Generate the hash for the value
    hashAndSaltForValue = makeHashAndSaltString(value, salt)
    return hashAndSalt == hashAndSaltForValue

def makeHashAndSaltString(value, salt = None):
    """
    Makes a hash from a given value and salt. If no salt is provided, one is generated.
    Salt must be of the correct length, or a ValueError will be thrown. The resulting
    string is of the form 'hash|salt'.

    value: the value for which to make a hash
    salt: the salt string (or None for a new salt)

    returns: the new hash
    """
    # Generate a salt if necesary
    if salt == None:
        salt = makeSalt()

    # Throw an exception if the salt does not have the correct length
    if len(salt) != saltLength:
        raise ValueError('Error: salt must be of length %s. Provided salt length was %s' % (saltLength, len(salt)))

    # Hash and return the value
    hash = hs.makeHash(value, salt)
    return hashAndSaltTemplate % (hash, salt)

def makeCookieForValue(value, salt = None):
    """
    Makes a cookie for the given value that contains the value, a hash of the value,
    and the salt.

    value: the value to make the cookie with
    salt: the salt string (or None for a new salt)

    returns: string
    """
    # Get the hash and salt
    hashAndSalt = makeHashAndSaltString(value, salt).split('|')
    hash = hashAndSalt[0]
    salt = hashAndSalt[1]

    # Make the cookie
    return cookieTemplate % (value, hash, salt)

def makeSalt():
    """
    Generates and returns a salt of random letters.

    returns: the new salt
    """
    return ''.join(random.choice(string.letters) for x in xrange(saltLength))
