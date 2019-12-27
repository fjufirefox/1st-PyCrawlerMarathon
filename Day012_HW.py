import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import re
# import pandas

# ettoday_url = 'https://www.ettoday.net/news/news-list.htm'
# ettoday_r = requests.get(ettoday_url, verify=False)
# ettoday_resp = ettoday_r.text
# ettoday_soup = BeautifulSoup(ettoday_resp, "html5lib")

now = datetime.now()

print(date.today())
print(datetime.now().strftime("%Y/%m/%d"))