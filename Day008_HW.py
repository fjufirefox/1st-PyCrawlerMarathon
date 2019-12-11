import requests
from bs4 import BeatifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.56 Safari/537.36 Edg/79.0.309.40'
}
# 利用 Request + BeatifulSoup 爬取下列兩個網站內容並解析：
# 1. Dcared 網址： https://www.dcard.tw/f
dcared_url = 'https://www.dcard.tw/f'
dcared_r = requests.get(dcared_url)
dcared_resp = dcared_r.text
dcared_soup = BeatifulSoup(dcared_resp, "html5lib")

print(dcared_resp)
print(dcared_soup)

# 2. 知乎： https://www.zhihu.com/explore
zhihu_url = 'https://www.zhihu.com/explore'
zhihu_r = requests.get(zhihu_url, headers=headers)
zhihu_resp = zhihu_r.text
zhihu_soup = BeatifulSoup(zhihu_resp, "html5lib")

print(zhihu_resp)
print(zhihu_soup)

# 並且回答下面問題：
# 1. Request 取回之後該怎麼取出資料，資料型態是什麼？
print('Request 取回之後該怎麼取出資料，資料型態是什麼？', type(dcared_resp), type(zhihu_resp))

# 2. 為什麼要使用 BeatifulSoup 處理？
print('為什麼要使用 BeatifulSoup 處理？', '解析HTML、XML⽂件、修復含有未閉合標籤等錯誤的⽂件')

# 3. 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？
print(' 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？', '加上 Header 即可取回正常資料')