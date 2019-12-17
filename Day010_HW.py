# 將之前用 requests + beatifulsoup 實作的方式，改寫成 grab + pyquery，並且比較有哪些地方不同。
import requests
from bs4 import beatifulsoup as bs
from grab import grab
from pyquery import pyquery

#requests + beatifulsoup
google_url = 'https://www.google.com'
google_r = requests.get(google_url)
google_resp = google_r.text
google_soup = bs(google_resp, "html5lib")

title = google_soup.title.string
print(type(title), title)

#grab + pyquery
google_r = grab().go(google_url)
google_resp = pyquery(google_r.body)

title = google_resp('title')
print(type(title), title.text())