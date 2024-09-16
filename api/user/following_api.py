import os
from typing import List
import requests
from enum import Enum
from api import logger
from api.user.user_object import Following

def get_following_data_by_user_id(user_id: str, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/user/id/{}/followings") -> List[Following]:
    url = base_url.format(user_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        data = response.json()
        
        followings = [Following(following_data) for following_data in data['data']['followings']]
        return followings
    
    except requests.exceptions.RequestException as err:
        logger.info(f"API request failed for user {user_id} with error: {err}")
    except Exception as err:
        logger.info(f"An unexpected error occurred: {err}")
    return None
