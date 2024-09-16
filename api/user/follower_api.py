import os
from typing import List
import requests
from enum import Enum
from api import logger
from api.user.user_object import Follower

def get_follower_data_by_user_id(user_id: str, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/user/id/{}/followers") -> List[Follower]:
    url = base_url.format(user_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        followers = [Follower(follower_data) for follower_data in data['data']['followers']]
        return followers
    except requests.exceptions.RequestException as err:
        logger.info(f"API request failed for user {user_id} with error: {err}")
    except Exception as err:
        logger.info(f"An unexpected error occurred: {err}")
    return None

