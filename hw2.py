from itertools import count
import bs4
import urllib.request as req


def getData(url):

    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 因為html不好解析，BeautifulSoup 協助解析html格式文件
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")  # 尋找所有class="title"的div標籤
    for title in titles:
        if title.a != None:  # 如果標題包含a標籤(沒有被刪除)，印出來
            print(title.a.string)
    nextLink = root.find("a", string="‹ 上頁")  # 抓取上一夜的連結，找到內文是‹ 上頁的a標籤
    return nextLink["href"]


pageURL = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 3:
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count += 1

    with open("movie.txt", "w", encoding="utf-8") as file:
        file.write(pageURL+"\n")
