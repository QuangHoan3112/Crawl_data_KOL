import os
from dotenv import load_dotenv
from api.user import user_api
import pandas as pd
from api.user import follower_api
from api.user import following_api 
from api.feed import user_feed_api
import json
import csv
# Load các biến môi trường từ file .env_sample
load_dotenv(dotenv_path='.env_sample')

# Lấy các giá trị từ biến môi trường
rapidapi_key = os.getenv('x-rapidapi-key')
rapidapi_host = os.getenv('x-rapidapi-host')

headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": rapidapi_host
}

if __name__ == '__main__':
    user_names = list(map(str, input("Nhập tên tài khoản KOL: ").split()))
    user_data_list = [] 

    output_file = 'kol_user_data.csv'

   
    for username in user_names:
        user = user_api.get_user_data_by_username(username, headers)  
        user_feed = user_feed_api.get_user_feed_by_username(username,headers)
        print(len(user_feed))
        with open("khoimy.json","w",encoding= "utf-8") as file:
            json.dump(user_feed,file,ensure_ascii=False,indent=4)
        if user:  
            user_data_list.append({
                "Nickname": user.nickname,       
                "Followers": user.follower_count, 
                "Total Favorited": user.total_favorited, 
                "UID": user.uid,            
                "Unique ID": user.unique_id,
                "user_feed": user_feed
            })
            with open(f"{username}.json","w",encoding= "utf-8") as file:
                json.dump(user_data_list,file,ensure_ascii=False,indent=4)
        


    if user_data_list:
        df = pd.DataFrame(user_data_list)

        # Ghi dữ liệu vào file CSV
        df.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"Dữ liệu đã được lưu vào {output_file}")
    else:
        print("Không tìm thấy thông tin người dùng.")

        '''print(user.__str__())
        user_id = user.uid  # Giả sử uid là user ID cần thiết
        print('Id người dùng là:', user_id)
        # Lấy dữ liệu followers từ follower_api
        followers = follower_api.get_follower_data_by_user_id(user_id, headers)
        
        if followers:
            print("Thông tin của Followers là: ")
            print("\n")
            for follower in followers:
                print(follower)
                print("\n" + "="*40 + "\n")
        else:
            print("No followers found or API request failed.")
        
        # Lấy dữ liệu following từ following_api
        followings = following_api.get_following_data_by_user_id(user_id, headers)
        
        if followings:
            print("Thông tin của Followings là: ")
            print("\n")
            for following in followings:
                print(following)
                print("\n" + "="*40 + "\n")  
        else:
            print("No following found or API request failed.")
    else:
        print("Failed to fetch user data.")'''
