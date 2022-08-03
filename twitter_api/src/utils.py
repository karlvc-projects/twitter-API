import requests
from authlib.integrations.requests_client import OAuth1Auth

from config import *

auth = OAuth1Auth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    token=TOKEN,
    token_secret=TOKEN_SECRET
)

def fetch_user_profile(username):
    fields = ",".join(("profile_image_url","description"))
    url = f"{TWITTER_BASE_URL}/2/users/by/username/{username}?user.fields={fields}"
    resp = requests.get(url, auth=auth)
    return resp.json()
