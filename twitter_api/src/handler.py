from response import success, error
from utils import fetch_user_profile, auth   
from config import *


def twitter(event: dict, _context: dict = {}) -> dict:
    try:
        if not event.get('pathParameters'):
            return 'No pathparameters are found'
        
        if not event['pathParameters'].get('username'):
            return 'No username is found'
        
        username = event['pathParameters']['username']
        response = fetch_user_profile(username)
        if message := response.get("errors"):
            return error(message)
        return success(response)
    except Exception as msg:
        return error(str(msg))