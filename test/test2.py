
# Using OAuth1Session
from requests_oauthlib import OAuth1Session

# Using OAuth1 auth helper
import requests
from requests_oauthlib import OAuth1

Consumer_Key="y7boBxoPz9ik4u1jSUVu0dpUz",
Consumer_Secret="mnxfxbKANvKooHJMFjMOY55gayUHNxasaeddaq00bjGyHT5u8t",
Access_Token="1552531590110396416-3KOpQsrYRS9Skh5lBgUb4GXZcxoTsZ",
Token_Secret="OvG7rseyOwfGJbMBTyG4FqReTDjiSLiIzZMfZ7qy5N5IZ"

request_token_url = 'https://api.twitter.com/oauth/request_token'
oauth = OAuth1Session(Consumer_Key, client_secret=Consumer_Secret)

fetch_response = oauth.fetch_request_token(request_token_url)
print(fetch_response)