"""
Нужно парсить страницу со свежими статьями (вот эту) и выбирать те статьи, в которых встречается хотя бы одно из
ключевых слов. Эти слова определяем в начале скрипта. Поиск вести по всей доступной preview-информации, т. е. по
информации, доступной с текущей страницы. Выведите в консоль список подходящих статей в формате:
<дата> – <заголовок> – <ссылка>.
с помощью bs4
"""

import random
import time

import bs4
import requests
from fake_headers import Headers

## Определяем список ключевых слов:
KEYWORDS = ["дизайн", "фото", "web", "python"]
URL = "https://habr.com/ru/articles"
URL_LINK = "https://habr.com"


def generate_headers():
    headers = Headers(os="win", browser="chrome")
    return headers.generate()


response = requests.get(URL, headers=generate_headers())
page = bs4.BeautifulSoup(response.text, "lxml")
tm_articles_list = page.find("div", class_="tm-articles-list")
articles = tm_articles_list.find_all("article")
articles_parsed = []

for article in articles:
    time_tag = article.find("time")
    h2_tag = article.find("h2")
    a_tag = h2_tag.find("a")

    article_date = time_tag["datetime"]
    article_title = a_tag.text
    article_link = f"{URL_LINK}{a_tag['href']}"

    time.sleep(random.randint(1, 5) * random.random() * 0.1)
    page_response = requests.get(article_link, headers=generate_headers())
    page_tag = bs4.BeautifulSoup(page_response.text, "lxml")
    body = page_tag.find("div", id="post-content-body").text
    article_parsed = {
        "date": article_date,
        "title": article_title,
        "link": article_link,
        "body": body,
    }
    articles_parsed.append(article_parsed)
if __name__ == "__main__":
    for keyword in KEYWORDS:
        print(f"Статьи, содержащие ключевое слово '{keyword}':")
        for article in articles_parsed:
            if keyword.lower() in article["body"].lower():
                print(f"{article['date']} - {article['title']} - {article['link']}")
        print()
