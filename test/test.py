import requests
from urllib.parse import quote as rawurlencode
import time
import string
import random
import operator
from hashlib import sha1
from hmac import new as hmac
import base64


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# personal Info - taken from https://www.mkmapi.eu/ws/documentation/API:Auth_Overview
mkmAppToken = 'bfaD9xOU0SXBhtBP'
mkmAppSecret = 'pChvrpp6AEOEwxBIIUBOvWcRG3X9xL4Y'
mkmAccessToken = 'lBY1xptUJ7ZJSK01x4fNwzw8kAe5b10Q'
mkmAccessSecret = 'hc1wJAOX02pGGJK2uAv1ZOiwS7I9Tpoe'

Consumer_Key="y7boBxoPz9ik4u1jSUVu0dpUz"
Consumer_Secret="mnxfxbKANvKooHJMFjMOY55gayUHNxasaeddaq00bjGyHT5u8t"
Access_Token="1552531590110396416-3KOpQsrYRS9Skh5lBgUb4GXZcxoTsZ"
Token_Secret="OvG7rseyOwfGJbMBTyG4FqReTDjiSLiIzZMfZ7qy5N5IZ"

# Url to access on mkm
# note that this deviates from the example in the header documentation (https://www.mkmapi.eu/ws/documentation/API:Auth_OAuthHeader) which uses
#accessUrl = 'https://www.mkmapi.eu/ws/v1.1/account'
username = 'Deepakp38197036'
accessUrl = f"https://api.twitter.com/2/users/by/username/{username}"

#Method for access

MyMethod = "GET"

baseString = MyMethod + "&" + rawurlencode(accessUrl) + "&"

# create a random string
# the documentation in https://www.mkmapi.eu/ws/documentation/API:Auth_OAuthHeader uses
#nonce = 53eb1f44909d6
nonce = id_generator(8)

# what time is it?
# the documentation in https://www.mkmapi.eu/ws/documentation/API:Auth_OAuthHeader uses
#now = 1407917892

now = str(int(time.time()))

MyOauthmethod = "HMAC-SHA1"
MyOauthver = "1.0"

# define Parameters and values, order doesn't matter
paramDict ={"oauth_consumer_key":Consumer_Key, "oauth_token" :Access_Token, "oauth_nonce":nonce, "oauth_timestamp":now, "oauth_signature_method":MyOauthmethod, "oauth_version":MyOauthver}

# sorting of parameters is done here
sorted_paramDict = sorted(paramDict.items(), key=operator.itemgetter(0))

#collect the full parameters string
paramStr = ''

for kv in sorted_paramDict:
    paramStr = paramStr + kv[0] + "=" + kv[1] + "&"


# and get rid of the trailing ampersand
paramStr = paramStr[:-1]


#concatenate request and oauth parameters
baseString = baseString + rawurlencode(paramStr)

# concatenate both keys
signingKey = rawurlencode(Consumer_Secret) + "&" + rawurlencode(Token_Secret)
# and create a hased signature with the key and the baseString

# .encode('base64')
Signature = base64.b64encode(hmac(signingKey.encode(), baseString.encode(), sha1).digest())[:-1]

print(Signature)
# construct the header from the parameters and the URL and the signature
MyHeader = 'OAuth ' + 'realm="' + accessUrl + '", ' 

for kv in sorted_paramDict:
    MyHeader += kv[0] + '="' + kv[1] + '",'

MyHeader += 'oauth_signature="' + str(Signature, 'UTF8').strip() +'"'

headers = {'Authorization': MyHeader}

# and now requests can do its magic (pun intended)

r = requests.get(accessUrl, headers=headers)

outjson = r.json()
print(outjson)