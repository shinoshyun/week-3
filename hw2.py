import bs4
import urllib.request as req
url = "https://www.ptt.cc/bbs/index.html"
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")
print(root.title)
