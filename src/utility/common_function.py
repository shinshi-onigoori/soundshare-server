import json
import os
from urllib import request

# API情報
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
YOUTUBE_API_HOST = 'https://www.googleapis.com/youtube/v3/videos'
YOUTUBE_API_KEY = os.getenv('OUTUP_YOUTUBE_API_KEY')

def get_video_info(video_id : str) -> dict:
    req_url = '{}/?part=snippet&id={}&key={}'.format(YOUTUBE_API_HOST, video_id, YOUTUBE_API_KEY)
    print(req_url)
    req = request.Request(url=req_url, method="GET")
    data = request.urlopen(url=req)
    return json.loads(data.read())

