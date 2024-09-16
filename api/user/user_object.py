from enum import Enum


class AccountType(Enum):
    UNKNOWN = 0 
    PERSONAL_ACC = 2 
    BUSINESS_ACC = 3 
        
class Avatar:
    def __init__(self, uri=None, url_list=None,width=None, height=None):
        self.uri = uri
        self.url_list = url_list if url_list is not None else []
        self.width = width
        self.height = height
        
        
class User:
    def __init__(self, data: dict) -> None:
        self.account_type = data['account_type'] if 'account_type' in data.keys() else -1
        self.__get_avatar(data)
        self.status = data['status'] if 'status' in data.keys() else None 
        self.status_code = data['status_code'] if 'status_code' in data.keys() else -1 
        self.follower_count = data['follower_count'] if 'follower_count' in data.keys() else -1 
        self.following_count = data['following_count'] if 'following_count' in data.keys() else -1 
        self.nickname = data['nickname'] if 'nickname' in data.keys() else None 
        self.original_musician = data['original_musician'] if 'original_musician' in data.keys() else None 
        self.privacy_setting = data['privacy_setting'] if 'privacy_setting' in data.keys() else None 
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data.keys() else None 
        self.share_info = data['share_info'] if 'share_info' in data.keys() else None 
        self.short_id = data['short_id'] if 'short_id' in data.keys() else None 
        self.signature_language = data['signature_language'] if 'signature_language' in data.keys() else None 
        self.tab_settings = data['tab_settings'] if 'tab_settings' in data.keys() else None  
        self.total_favorited = data['total_favorited'] if 'total_favorited' in data.keys() else None  
        self.uid = data['uid'] if 'uid' in data.keys() else None  
        self.unique_id = data['unique_id'] if 'unique_id' in data.keys() else None 
        self.verification_type = data['verification_type'] if 'verification_type' in data.keys() else -1 
        self.video_icon = Avatar(**data['video_icon']) if 'video_icon' in data.keys() else None 
        pass
    
    def __get_avatar(self, data: dict):
        if 'avatar_larger' in data.keys():
            self.avatar = Avatar(**(data['avatar_larger']))
        elif 'avatar_medium' in data.keys():
            self.avatar = Avatar(**(data['avatar_medium']))
        elif 'avatar_300x300' in data.keys():
            self.avatar = Avatar(**(data['avatar_300x300']))
        elif 'avatar_168x168' in data.keys():
            self.avatar = Avatar(**(data['avatar_168x168']))
        elif 'avatar_thumb' in data.keys():
            self.avatar = Avatar(**(data['avatar_thumb']))
        else:
            self.avatar = None 
            
            
    def __str__(self) -> str:
        output_string = (
            f"Status: {self.status}\n" + 
            f"Status code: {self.status_code}\n" + 
            f"Follower count: {self.follower_count}\n" + 
            f"Following count: {self.following_count}\n" + 
            f"Nickname: {self.nickname}\n" + 
            f"Original musician: {self.original_musician}\n" + 
            f"Privacy setting: {self.privacy_setting}\n" + 
            f"Sec UID: {self.sec_uid}\n" + 
            f"Share info: {self.share_info}\n" + 
            f"Short ID: {self.short_id}\n" +
            f"Signature language: {self.signature_language}\n" + 
            f"Tab settings: {self.tab_settings}\n" + 
            f"Total favorited: {self.total_favorited}\n" + 
            f"UID: {self.uid}\n" + 
            f"Unique ID: {self.unique_id}\n" + 
            f"Verification type: {self.verification_type}\n" + 
            "\nAvatar:\n" + 
            ((f"URI: {self.avatar.uri}\n" + 
            "URL list:\n"
            + "\n".join(self.avatar.url_list) + "\n") if self.avatar is not None else "None\n") + 
            "\nVideo icon:\n" + 
            ((f"URI: {self.video_icon.uri}\n" + 
            "URL list:\n"
            + "\n".join(self.video_icon.url_list)) if self.video_icon is not None else "None\n") 
        )
        return output_string
    

class Follower:
    def __init__(self, data: dict) -> None:
        self.__get_avatar(data)
        self.status = data['status'] if 'status' in data else None 
        self.status_code = data['status_code'] if 'status_code' in data else -1 
        self.follower_count = data['follower_count'] if 'follower_count' in data else -1 
        self.favoriting_count = data['favoriting_count'] if "favoriting_count" in data else -1
        self.ins_id = data['ins_id'] if 'ins_id' in data else None
        self.following_count = data['following_count'] if 'following_count' in data else -1 
        self.language = data['language'] if 'language' in data else -1
        self.nickname = data['nickname'] if 'nickname' in data else None
        self.original_musician = data['original_musician'] if 'original_musician' in data else None 
        self.region = data['region'] if 'region' in data else None
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else None 
        self.awene_count = data['awene_count'] if'awene_count' in data else -1
        self.share_info = data['share_info'] if 'share_info' in data else None 
        self.short_id = data['short_id'] if 'short_id' in data else None 
        self.signature = data['signature'] if 'signature' in data else None 
        self.total_favorited = data['total_favorited'] if 'total_favorited' in data else None  
        self.uid = data['uid'] if 'uid' in data else None  
        self.unique_id = data['unique_id'] if 'unique_id' in data else None 
        self.unique_id_modify_time = data['unique_id_modify_time'] if 'unique_id_modify_time' in data else -1
        self.user_mode = data['user_mode'] if 'user_mode' in data else -1
        self.user_rate = data['user_rate'] if 'user_rate' in data else -1
        self.video_icon = Avatar(**data['video_icon']) if 'video_icon' in data else None 
        self.youtube_channel_id = data['youtube_channel_id'] if 'youtube_channel_id' in data else None
        self.youtube_channel_title = data['youtube_channel_title'] if 'youtube_channel_title' in data else None

    def __get_avatar(self, data: dict):
        if 'avatar_larger' in data:
            self.avatar = Avatar(**data['avatar_larger'])
        elif 'avatar_medium' in data:
            self.avatar = Avatar(**data['avatar_medium'])
        elif 'avatar_300x300' in data:
            self.avatar = Avatar(**data['avatar_300x300'])
        elif 'avatar_168x168' in data:
            self.avatar = Avatar(**data['avatar_168x168'])
        elif 'avatar_thumb' in data:
            self.avatar = Avatar(**data['avatar_thumb'])
        else:
            self.avatar = None 

    def __str__(self) -> str:
        output_list = [
            f"Status: {self.status}",
            f"Status code: {self.status_code}",
            f"Aweme count: {self.awene_count}",
            f"Follower count: {self.follower_count}",
            f"Following count: {self.following_count}",
            f"Favoriting count: {self.favoriting_count}",
            f"Language: {self.language}",
            f"Ins ID: {self.ins_id}",
            f"Nickname: {self.nickname}",
            f"Original musician: {self.original_musician}",
            f"Sec UID: {self.sec_uid}",
            f"Share info: {self.share_info}",
            f"Short ID: {self.short_id}",
            f"Signature: {self.signature}",
            f"Total favorited: {self.total_favorited}",
            f"UID: {self.uid}",
            f"Unique ID: {self.unique_id}",
            f"Unique ID modify time: {self.unique_id_modify_time}",
            f"User mode: {self.user_mode}",
            f"User rate: {self.user_rate}",
            f"Youtube Channel ID: {self.youtube_channel_id}",
            f"Youtube Channel title: {self.youtube_channel_title}",
            "Video icon:",
            (f"URI: {self.video_icon.uri}\nURL list:\n" + "\n".join(self.video_icon.url_list)) if self.video_icon else "None"
        ]
        return "\n".join(output_list)


class Following:
    def __init__(self, data: dict) -> None:
        self.__get_avatar(data)
        self.status = data['status'] if 'status' in data else None 
        self.status_code = data['status_code'] if 'status_code' in data else -1 
        self.follower_count = data['follower_count'] if 'follower_count' in data else -1 
        self.favoriting_count = data['favoriting_count'] if "favoriting_count" in data else -1
        self.ins_id = data['ins_id'] if 'ins_id' in data else None
        self.following_count = data['following_count'] if 'following_count' in data else -1 
        self.language = data['language'] if 'language' in data else -1
        self.nickname = data['nickname'] if 'nickname' in data else None
        self.original_musician = data['original_musician'] if 'original_musician' in data else None 
        self.region = data['region'] if 'region' in data else None
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else None 
        self.awene_count = data['awene_count'] if'awene_count' in data else -1
        self.share_info = data['share_info'] if 'share_info' in data else None 
        self.short_id = data['short_id'] if 'short_id' in data else None 
        self.signature = data['signature'] if 'signature' in data else None 
        self.total_favorited = data['total_favorited'] if 'total_favorited' in data else None  
        self.uid = data['uid'] if 'uid' in data else None  
        self.unique_id = data['unique_id'] if 'unique_id' in data else None 
        self.unique_id_modify_time = data['unique_id_modify_time'] if 'unique_id_modify_time' in data else -1
        self.user_mode = data['user_mode'] if 'user_mode' in data else -1
        self.user_rate = data['user_rate'] if 'user_rate' in data else -1
        self.video_icon = Avatar(**data['video_icon']) if 'video_icon' in data else None 
        self.youtube_channel_id = data['youtube_channel_id'] if 'youtube_channel_id' in data else None
        self.youtube_channel_title = data['youtube_channel_title'] if 'youtube_channel_title' in data else None

    def __get_avatar(self, data: dict):
        if 'avatar_larger' in data:
            self.avatar = Avatar(**data['avatar_larger'])
        elif 'avatar_medium' in data:
            self.avatar = Avatar(**data['avatar_medium'])
        elif 'avatar_300x300' in data:
            self.avatar = Avatar(**data['avatar_300x300'])
        elif 'avatar_168x168' in data:
            self.avatar = Avatar(**data['avatar_168x168'])
        elif 'avatar_thumb' in data:
            self.avatar = Avatar(**data['avatar_thumb'])
        else:
            self.avatar = None 

    def __str__(self) -> str:
        output_list = [
            f"Status: {self.status}",
            f"Status code: {self.status_code}",
            f"Aweme count: {self.awene_count}",
            f"Follower count: {self.follower_count}",
            f"Following count: {self.following_count}",
            f"Favoriting count: {self.favoriting_count}",
            f"Language: {self.language}",
            f"Ins ID: {self.ins_id}",
            f"Nickname: {self.nickname}",
            f"Original musician: {self.original_musician}",
            f"Sec UID: {self.sec_uid}",
            f"Share info: {self.share_info}",
            f"Short ID: {self.short_id}",
            f"Signature: {self.signature}",
            f"Total favorited: {self.total_favorited}",
            f"UID: {self.uid}",
            f"Unique ID: {self.unique_id}",
            f"Unique ID modify time: {self.unique_id_modify_time}",
            f"User mode: {self.user_mode}",
            f"User rate: {self.user_rate}",
            f"Youtube Channel ID: {self.youtube_channel_id}",
            f"Youtube Channel title: {self.youtube_channel_title}",
            "Avatar:",
            (f"URI: {self.avatar.uri}\nURL list:\n" + "\n".join(self.avatar.url_list)) if self.avatar else "None",
            "Video icon:",
            (f"URI: {self.video_icon.uri}\nURL list:\n" + "\n".join(self.video_icon.url_list)) if self.video_icon else "None"
        ]
        return "\n".join(output_list)