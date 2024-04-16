import requests
import json

uid = '1437582453'
room_id = '22816111'
url = f'https://api.live.bilibili.com/room/v1/Room/get_info?uid={uid}&room_id={room_id}'

response = requests.get(url)
data = response.json()
print(data)