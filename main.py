import os 
from api.user import user_api
from dotenv import load_dotenv

load_dotenv() 

headers = {
    "x-rapidapi-key": os.environ.get("x-rapidapi-key"),
    "x-rapidapi-host": os.environ.get("x-rapidapi-host")
}
if __name__ == '__main__':
    user_name = "elyitclean"
    user = user_api.get_user_data_by_username(user_name, headers)
    
    print(user.__str__())