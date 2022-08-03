import requests
import time
import uuid
from hmac import new as hmac
from hashlib import sha1

Consumer_Key="y7boBxoPz9ik4u1jSUVu0dpUz"
Consumer_Secret="mnxfxbKANvKooHJMFjMOY55gayUHNxasaeddaq00bjGyHT5u8t"
Access_Token="1552531590110396416-3KOpQsrYRS9Skh5lBgUb4GXZcxoTsZ"
Token_Secret="OvG7rseyOwfGJbMBTyG4FqReTDjiSLiIzZMfZ7qy5N5IZ"



username = 'Deepakp38197036'
timestamp = int(time.time())
nonce = uuid.uuid4().hex
url = f"https://api.twitter.com/2/users/by/username/{username}"
# username = input('Enter your twitter username: ')
# params = {"user.fields":"profile_image_url"}
params = '?user.fields=profile_image_url'

params = f"include_entities=true&oauth_consumer_key={Consumer_Key}&oauth_nonce={nonce}&oauth_signature_method=HMAC-SHA1&oauth_timestamp={timestamp}&oauth_token={Access_Token}&oauth_version=1.0"
def generate_base_signature():
    output = 'GET'
    output+='&'
    output+=requests.utils.quote(url)
    # output+='&'
    # output+=requests.utils.quote(params)
    return output
def signin_key():
    return requests.utils.quote(Consumer_Secret)+'&'+requests.utils.quote(Token_Secret)

def generate_signature():
    base_signature =generate_base_signature()
    key = signin_key()
    return hmac(key.encode(), base_signature.encode(), sha1).hexdigest()
signature = generate_signature()
print(signature,'generate_base_...................')
headers = {
    "Authorization":f'OAuth oauth_consumer_key={Consumer_Key},oauth_token={Access_Token},oauth_signature_method="HMAC-SHA1",oauth_timestamp="1659008249",oauth_nonce="P0wd4bgRWwg",oauth_version="1.0",oauth_signature={signature}'
}
response = requests.get(url, headers=headers)
print(response.text)
if response.status_code == 200:
    print(response.text)
else:
    print(f'No twitter account found related to this username:- {username}')








