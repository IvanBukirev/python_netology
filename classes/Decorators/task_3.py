"""
Применить написанный логгер к приложению из любого предыдущего д/з.
"""
import os

import bs4
import requests
from fake_headers import Headers

from classes.Decorators.task_2 import logger

KEYWORDS = ["дизайн", "фото", "web", "python", "Docker", "Linux"]
URL = "https://habr.com/ru/articles"
URL_LINK = "https://habr.com"
PATH_TO_LOG = "task_3.log"


@logger(PATH_TO_LOG)
def generate_headers():
    headers = Headers(os="win", browser="chrome")
    return headers.generate()


@logger(PATH_TO_LOG)
def get_articles(url, headers):
    response = requests.get(url, headers)
    page = bs4.BeautifulSoup(response.text, "lxml")
    tm_articles_list = page.find("div", class_="tm-articles-list")
    articles = tm_articles_list.find_all("article")
    return articles


@logger(PATH_TO_LOG)
def get_articles_lst():
    articles_lst = []
    for article in get_articles(URL, generate_headers()):
        time_tag = article.find("time")
        h2_tag = article.find("h2")
        a_tag = h2_tag.find("a")

        article_date = time_tag["datetime"]
        article_title = a_tag.text
        article_link = f"{URL_LINK}{a_tag['href']}"

        articles_parsed = {"date": article_date, "title": article_title, "link": article_link}
        articles_lst.append(articles_parsed)
    return articles_lst


@logger(PATH_TO_LOG)
def find_articles(keywords):
    for keyword in keywords:
        print(f"Статьи, содержащие ключевое слово '{keyword}':")
        for article in get_articles_lst():
            if keyword.lower() in article["title"].lower():
                print(f"{article['date']} - {article['title']} - {article['link']}")
        print()


if __name__ == "__main__":
    if os.path.exists(PATH_TO_LOG):
        os.remove(PATH_TO_LOG)
    find_articles(KEYWORDS)
