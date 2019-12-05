# 1.比較一下範例檔案中的「r.text」與「json.loads(r.text)」讀出來的內容有什麼差異
import requests
import json
r = requests.get('https://api.github.com/events')
print(type(r.text), type(json.loads(r.text)))
# 2.自行尋找一個合適的 API 接口做練習，並且查看其回傳內容：
# 	https://cat-fact.herokuapp.com/facts (來源：https://alexwohlbruck.github.io/cat-facts/)
# 	http://odata.wra.gov.tw/v4/RealtimeWaterLevel (來源：https://data.gov.tw/dataset/25768)
cat_r = requests.get('https://cat-fact.herokuapp.com/facts', params=None)
json.loads(cat_r.text,
           encoding=None,
           cls=None,
           object_hook=None,
           parse_float=None,
           parse_int=None,
           parse_constant=None,
           object_pairs_hook=None)
