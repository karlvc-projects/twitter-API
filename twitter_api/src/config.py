import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
TOKEN = os.environ["TOKEN"]
TOKEN_SECRET = os.environ["TOKEN_SECRET"]
TWITTER_BASE_URL = os.environ["TWITTER_BASE_URL"]

