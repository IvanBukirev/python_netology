"""
Нужно парсить страницу со свежими статьями (вот эту) и выбирать те статьи, в которых встречается хотя бы одно из
ключевых слов. Эти слова определяем в начале скрипта. Поиск вести по всей доступной preview-информации, т. е. по
информации, доступной с текущей страницы. Выведите в консоль список подходящих статей в формате:
<дата> – <заголовок> – <ссылка>.
с помощью selenium
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

## Определяем список ключевых слов:
KEYWORDS = ["дизайн", "фото", "web", "python"]
URL = "https://habr.com/ru/articles/"


def wait_element(driver_or_tag, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(driver_or_tag, delay_seconds).until(
        presence_of_element_located((by, value))
    )


path = ChromeDriverManager().install()

service = Service(executable_path=path)

driver = Chrome(service=service)

driver.get(URL)
list_tag = driver.find_element(By.CLASS_NAME, "tm-articles-list")
tags_articles = list_tag.find_elements(By.TAG_NAME, "article")
parsed_data = []

for tag in tags_articles:
    time_tag = wait_element(tag, 1, By.TAG_NAME, "time")
    h2_tag = wait_element(tag, 1, By.TAG_NAME, "h2")
    a_tag = wait_element(h2_tag, 1, By.TAG_NAME, "a")

    title = a_tag.text
    date = time_tag.get_attribute("datetime")
    link = a_tag.get_attribute("href")

    parsed_article = {"date": date, "title": title, "link": link}
    parsed_data.append(parsed_article)

for article in parsed_data:
    driver.get(article["link"])
    body_tag = wait_element(driver, 1, By.ID, "post-content-body")
    article["body"] = body_tag.text

if __name__ == "__main__":
    for keyword in KEYWORDS:
        print(f"Статьи, содержащие ключевое слово '{keyword}':")
        for article in parsed_data:
            if keyword.lower() in article["body"].lower():
                print(f"{article['date']} - {article['title']} - {article['link']}")
        print()
