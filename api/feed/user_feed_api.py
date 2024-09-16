import os
import requests
from api import logger
from enum import Enum


def get_user_feed_by_username(username, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/user/{}/feed"):
    url = base_url.format(username)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        feed_list = []
        feeds = data['data']['aweme_list']
        for feed in feeds:
            feed_info = {}
            feed_info["statistics"] = feed["statistics"]
            feed_info["release_date"] = decode_unixtime(feed["create_time"])
            feed_list.append(feed_info)
        return feed_list
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")
        return None

from datetime import datetime
def decode_unixtime(time):
    time = int(time)
    return datetime.fromtimestamp(time).strftime('%d-%m-%Y')