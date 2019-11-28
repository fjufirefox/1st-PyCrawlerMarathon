#1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
#a.檔案:csv、json、xml。
#b.API:提供程式化的連接接口，可以選擇資料中要讀取的特定部份，而不需要把整批資料事先完整下載回來。
#c.爬蟲:利用爬蟲程式，將網頁的資料解析所需要的部份。

#2.（實作）完成一個程式，需滿足下列需求：
import os
import chardet
from urllib.request import urlretrieve

#「下載指定檔案到 Data 資料夾，
#存成檔名 Homework.txt」的檔案網址：https://www.w3.org/TR/PNG/iso_8859-1.txt 或任一個 .txt 的檔案網址
#

folderpath = "Data"
filename = "Homework.txt"
filepath = "./" + folderpath + "/" + filename

os.makedirs(folderpath, exist_ok=True)

txtfile_url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"

urlretrieve(txtfile_url, filepath)
#檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
#
if os.path.isfile(filepath):
    #將「Hello World」字串覆寫到 Homework.txt 檔案
    #
    f = open(filepath, mode='w')
    f.write("Hello World")
    f.close()
#檢查 Homework.txt 檔案字數是否符合 Hello World 字數
if os.path.isfile(filepath):
    f = open(filepath, mode='r')
    data = f.read()
    if len(data) == len("Hello World"):
        print('符合 Hello World 字數')