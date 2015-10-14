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
import hashSecret as hs

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
"""
Returns the username from the cookie if the cookie is valid, or None if the cookie
is invalid.

cookie: the cookie to attempt to get the user from

returns string (or None)
"""
def tryGetUserFromCookie(cookie):
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


"""
Checks the given value against the hash and salt. Will throw a ValueError if
the hashAndSalt string is not in the correct form.

value: the value to check
hashAndSalt: the hash and salt to check the value against

returns: bool
"""
def isHashAndSaltValidForValue(value, hashAndSalt):
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

"""
Makes a hash from a given value and salt. If no salt is provided, one is generated.
Salt must be of the correct length, or a ValueError will be thrown. The resulting
string is of the form 'hash|salt'.

value: the value for which to make a hash
salt: the salt string (or None for a new salt)

returns: the new hash
"""
def makeHashAndSaltString(value, salt = None):
    # Generate a salt if necesary
    if salt == None:
        salt = makeSalt()

    # Throw an exception if the salt does not have the correct length
    if len(salt) != saltLength:
        raise ValueError('Error: salt must be of length %s. Provided salt length was %s' % (saltLength, len(salt)))

    # Hash and return the value
    hash = hs.makeHash(value, salt)
    return hashAndSaltTemplate % (hash, salt)

"""
Makes a cookie for the given value that contains the value, a hash of the value,
and the salt.

value: the value to make the cookie with
salt: the salt string (or None for a new salt)

returns: string
"""
def makeCookieForValue(value, salt = None):
    # Get the hash and salt
    hashAndSalt = makeHashAndSaltString(value, salt).split('|')
    hash = hashAndSalt[0]
    salt = hashAndSalt[1]

    # Make the cookie
    return cookieTemplate % (value, hash, salt)

"""
Generates and returns a salt of random letters.

returns: the new salt
"""
def makeSalt():
    return ''.join(random.choice(string.letters) for x in xrange(saltLength))
