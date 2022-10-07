import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)
