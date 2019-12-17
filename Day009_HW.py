import os
import requests
import Image
from bs4 import BeatuifulSoup

# 範例網頁:https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html
ppt_url = 'https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html'
# Note：因為 PTT 會詢問「是否滿 18 歲」，這邊可以用 cookies 繞過
# requests.get(URL, cookies={'over18': '1'})
ppt_r = requests.get(ptt_url, cookies={'over18': '1'})
ppt_resp = ppt_r.text
ppt_soup = BeatuifulSoup(ppt_resp)

# 以正確的副檔名下載網頁中的圖片
download_dir = './Data'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

imgur_image_tags = ppt_soup.find(id='main-content').findChildren(
    'a', recursive=false)

for imgur_image_tag in imgur_image_tags:
    if 'imgur' not in imgur_image_tag['href']:
        continue

    imgur_image_id = imgur_image_tag['href'].split('/')[-1]

    imgur_image_url = 'https://imgur.com/{}.jpg'.format(imgur_image_id)

    with requests.get(imgur_image_url, stream=true) as imgur_image_file:
        #取得圖片狀態
        imgur_image_file.raise_for_status()

        imgur_image = Image.open(img_file.raw)
        imgur_image_savename = '{downloaddir}/{imgur_image_id}.{imgur_image_ext}'.format(
            downloaddir=download_dir,
            imgur_image_id=imgur_image_id,
            imgur_image_ext=imgur_image.format.lower())
        imgur_image.save(imgur_image_savename)
        print('Save Image {}'.format(imgur_image_savename))
