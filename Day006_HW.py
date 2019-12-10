import json
import requests
from time import ctime

# 根據範例提供的 API 網址 ，完成以下問題：
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.56 Safari/537.36 Edg/79.0.309.40'
}

r = requests.get(
    'https://www.zhihu.com/api/v4/questions/55493026/answers',
    headers=headers,
)

resp = r.text
# 1. 取出知乎問題發問時間
file = json.loads(r.text)
print('資料源有什麼欄位', file[1].key())
print('知乎問題發問時間', ctime(float(file['data'][0]['question']['created'])))

# 2. 取出第一筆與最後一筆回答的時間
print('取出第一筆回答的時間', ctime(float(file['data'][2]['question']['created'])))
print('取出最後一筆回答的時間', ctime(float(file['data'][-1]['question']['created'])))
