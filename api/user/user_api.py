import os
import requests
from api import logger
from enum import Enum
from api.user.user_object import User

def get_user_data_by_username(username, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/user/{}") -> User:
    url = base_url.format(username)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        user = User(data['data']['user'])
        return user
    except requests.exceptions.RequestException as err:
        logger.info(f"API request failed for user {username} with error: {err}")
    except Exception as err:
        logger.info(f"An unexpected error occurred: {err}")
    return None
