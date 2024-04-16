import requests
import json
from typing import Dict

HEADERS: Dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
def get_info_live(uid,room_id):
    live_status={}
    url = f'https://api.live.bilibili.com/room/v1/Room/get_info?uid={uid}&room_id={room_id}'
    response = requests.get(url,headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
                info = data['data']
                live_status[uid] = {
                    'live_status': info['live_status'],
                    'title': info['title'],
                    'uid': uid,
                    'room_id': room_id,
                    'face': info['user_cover'],
                    'url': f'https://live.bilibili.com/{room_id}'
                }

    else:
        print("請求失敗，狀態碼：", response.status_code)        
    return live_status

def get_info(uid):
    a = {}
    bilibili_info_api_url = f'https://api.bilibili.com/x/web-interface/card?mid={uid}'
    response = requests.get(bilibili_info_api_url,headers=HEADERS)
    data = response.json()
    if data['code'] == 0:
        info = data['data']
        a[uid]={
            'name': info['card']['name'],
            'icon': info['card']['face'],
        }
    return a



