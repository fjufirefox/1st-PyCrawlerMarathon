#比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異
#
#根據範例檔案的結果：
#
import csv
from array import array

folderpath = "Data"
filename = "example.csv"
filepath = "./" + folderpath + "/" + filename

# 列出CSV全部的資料
# with open(filepath,
#           mode='r',
#           buffering=-1,
#           encoding='UTF-8',
#           errors=None,
#           newline=None,
#           closefd=True) as cvsfile:
#     rows = csv.reader(cvsfile)
#     for row in rows:
#         print(row)

#1. 取出班次一的每一個時間，印出來就好
#
# with open(filepath,
#           mode='r',
#           buffering=-1,
#           encoding='UTF-8',
#           errors=None,
#           newline=None,
#           closefd=True) as cvsfile:
#     rows = csv.reader(cvsfile)
#     for row in rows:
#         print(row[5])

#2. 將班次一的每一個時間用一個變數保存
#
data = array()
with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as cvsfile:

    rows = csv.reader(filepath)
    for row in rows:
        data.append(row[5])
print(data)

#3. 將所有班次和其每一個時間用一個變數保存
#
#(Hint： 2&3 要想一下用什麼的資料型態做整理比較適合)