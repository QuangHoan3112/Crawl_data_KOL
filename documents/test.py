import requests
import json

with open('tiktok_user_singer.khoimy_feed.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)

user = data1['data']['user']
user_data_list = []  # List để lưu thông tin của từng user

# Đặt tên file CSV
output_file = 'kol_khoimy_data.csv'

user_data_list.append({
                "Nickname": user.nickname,       
                "Followers":user.follower_count, 
                "Total Favorited": user.total_favorited, 
                "UID": user.uid,            
                "Unique ID": user.unique_id       
            })



