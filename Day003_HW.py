# 比較一下範例檔案中的「File I/O」與「xmltodict」讀出來的內容有什麼差異
# 根據範例檔案的結果：
import os

filepath = './Data/xml/64_72hr_CH.xml'

with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as fio:
    xml = fio.read()
    print(xml)

import xmltodict
with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as fxml:
    xmldict = dict(xmltodict.parse(fxml.read()))
    print(xmldict)
# # 1. 請問高雄市有多少地區有溫度資料？

count_num = 0
with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as fd:
    doc = xmltodict.parse(fd.read())

sect_with_tempers = doc["cwbopendata"]["dataset"]["locations"]["location"]
for sect_with_temper in sect_with_tempers:
    for weatherElement in sect_with_temper["weatherElement"]:
        if weatherElement["description"] == '溫度':
            count_num = count_num + 1

# print('高雄市有%s地區有溫度資料' % count_num)

# 2. 請取出每一個地區所記錄的第一個時間點跟溫度
for sect_with_temper in sect_with_tempers:
    for weatherElement in sect_with_temper["weatherElement"]:
        if weatherElement["description"] == '溫度':
            print(sect_with_temper["locationName"],
                  weatherElement["time"][0]["dataTime"],
                  weatherElement["time"][0]["elementValue"]["value"],
                  weatherElement["time"][0]["elementValue"]["measures"])

# 3. 請取出第一個地區所記錄的每一個時間點跟溫度
first_area = doc['cwbopendata']['dataset']['locations']['location'][0][
    'locationName']

first_tempers = doc['cwbopendata']['dataset']['locations']['location'][0][
    'weatherElement'][0]['time']

for first_temper in first_tempers:
    print(first_area, '時間:', first_temper['dataTime'], '溫度',
          first_temper['elementValue']['value'], '°C')