#比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異
#
#根據範例檔案的結果：
#
import csv

folderpath = "Data"
filename = "example.csv"
filepath = "./" + folderpath + "/" + filename

# 列出CSV全部的資料
with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as cvsfile:
    rows = csv.reader(cvsfile)
    for row in rows:
        print(row)

#1. 取出班次一的每一個時間，印出來就好
#
with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as cvsfile:
    rows = csv.reader(cvsfile)
    for row in rows:
        print(row[5])

#2. 將班次一的每一個時間用一個變數保存
#
data = []
with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as cvsfile:

    rows = csv.reader(cvsfile)
    for row in rows:
        data.append(row[5])
print(data)

#3. 將所有班次和其每一個時間用一個變數保存
#
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []
d8 = []
d9 = []
d10 = []
d11 = []

with open(filepath,
          mode='r',
          buffering=-1,
          encoding='UTF-8',
          errors=None,
          newline=None,
          closefd=True) as cvsfile:
    rows = csv.reader(cvsfile)
    for row in rows:
        d1.append(row[5])
        d2.append(row[6])
        d3.append(row[7])
        d4.append(row[8])
        d5.append(row[9])
        d6.append(row[10])
        d7.append(row[11])
        d8.append(row[12])
        d9.append(row[13])
        d10.append(row[14])
        d11.append(row[15])

data = {}
data[d1[0]] = d1[1:]
data[d2[0]] = d2[1:]
data[d3[0]] = d3[1:]
data[d4[0]] = d4[1:]
data[d5[0]] = d5[1:]
data[d6[0]] = d6[1:]
data[d7[0]] = d7[1:]
data[d8[0]] = d8[1:]
data[d9[0]] = d9[1:]
data[d10[0]] = d10[1:]
data[d11[0]] = d11[1:]

print(data)
#(Hint： 2&3 要想一下用什麼的資料型態做整理比較適合)
# json