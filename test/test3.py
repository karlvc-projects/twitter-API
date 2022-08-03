import requests
from authlib.integrations.requests_client import OAuth1Auth

auth = OAuth1Auth(
    client_id='y7boBxoPz9ik4u1jSUVu0dpUz',
    client_secret='mnxfxbKANvKooHJMFjMOY55gayUHNxasaeddaq00bjGyHT5u8t',
    token='1552531590110396416-3KOpQsrYRS9Skh5lBgUb4GXZcxoTsZ',
    token_secret='OvG7rseyOwfGJbMBTyG4FqReTDjiSLiIzZMfZ7qy5N5IZ'
)

username = 'Deepakp38197036'
url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url"

resp = requests.get(url, auth=auth)
print(resp.text)