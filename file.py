import urllib.request as reguest
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with reguest.urlopen(src) as response:
    data = json.load(response)
# print(data)
clist = data["result"]["results"]

with open("data.csv", "w", encoding="utf-8") as file:
    for information in clist:
        year = information["xpostDate"][:4]
        for year in range(2015, 2023):
            print(year)
    # file.write(information["stitle"]+", " +
    #            information["address"][5:8]+", " +
    #            information["longitude"]+", " +
    #            information["latitude"]+", " +
    #            information["file"]url[0]+", " + "\n")
