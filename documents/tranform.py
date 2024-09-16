import json

class ChallengeInfo:
    def __init__(self, data: dict) -> None:
        self.view_count = data['view_count'] if 'view_count' in data else None
        self.type = data['type'] if 'type' in data else None
        self.user_count = data['user_count'] if 'user_count' in data else None
        self.cid = data['cid'] if 'cid' in data else None
        self.cha_name = data['cha_name'] if 'cha_name' in data else None

    def __str__(self) -> str:
        return (
            f"ChallengeInfo(\n"
            f"  view_count: {self.view_count},\n"
            f"  type: {self.type},\n"
            f"  user_count: {self.user_count},\n"
            f"  cid: '{self.cid}',\n"
            f"  cha_name: '{self.cha_name}'\n"
            f")"
        )

class ResponseData:
    def __init__(self, data: dict) -> None:
        self.ch_info = ChallengeInfo(data['ch_info']) if 'ch_info' in data else None
        self.status_code = data['status_code'] if 'status_code' in data else None

    def __str__(self) -> str:
        return (
            f"ResponseData: \n"
            f"  ch_info: {self.ch_info},\n"
            f"  status_code: {self.status_code}\n"
            
        )

class Hastag:
    def __init__(self, data: dict) -> None:
        self.status = data['status'] if 'status' in data else None
        self.data = ResponseData(data['data']) if 'data' in data else None

    def __str__(self) -> str:
        return (
            f"Hastag Info: (\n"
            f"  status: '{self.status}',\n"
            f"  data: {self.data}\n"
            f")"
        )

# Đọc dữ liệu từ tệp JSON
output_file = "tiktok_hastag_challenge_data.json"
with open(output_file, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Chuyển đổi dữ liệu JSON thành đối tượng Python
api_response = Hastag(json_data)

# In thông tin từ đối tượng
print(api_response)
