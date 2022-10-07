import re
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

clist = data["result"]["results"]
count = 0
with open("data.csv", "w", encoding="utf-8") as file:
    for information in clist:
        # 用 regular expressions 來去篩選  
        jpg = re.split("jpg|JPG",information["file"])
        date = re.split("/",information["xpostDate"])
        # 程式碼示例演示如何使用列表推導方法將列表從字串轉換為整數
        int_list = [int(i) for i in date]
        if int_list[0] >= 2015:
            file.write(information["stitle"]+", " +
                       information["address"][5:8]+", " +
                       information["longitude"] + ", " +
                       information["latitude"]+", " +
                       jpg[0]+"jpg"+"\n")

