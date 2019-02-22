import requests


def getUrl(url):
    response = requests.get(url)
    html = response.content
    html_encode = str(html, "utf-8")
    print(html_encode)


if __name__ == '__main__':    getUrl("https://www.baidu.com")
