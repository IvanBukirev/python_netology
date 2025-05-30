import os
import unittest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv("../../.env")


class TestYandexAuth(unittest.TestCase):
    """
    Класс для тестирования авторизации на сайте yandex.ru.
    """

    def setUp(self):
        """
        Метод для настройки окружения перед запуском тестов.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://passport.yandex.ru/auth"
        self.login = os.getenv("YANDEX_LOGIN")
        self.password = os.getenv("YANDEX_PASSWORD")

        if not self.login or not self.password:
            self.skipTest("Что-то не так с логином или паролем")

    def test_authorization(self):
        """
        Проверка успешной авторизации
        """
        driver = self.driver
        driver.get(self.base_url)

        # Вводим логин
        login_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "passp-field-phone"))
        )
        login_input.send_keys(self.login)
        driver.find_element(By.ID, "passp:sign-in").click()

        # Вводим пароль
        password_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "passp-field-passwd"))
        )
        password_input.send_keys(self.password)
        driver.find_element(By.ID, "passp:sign-in").click()

        # Шаг 3: Проверка успешной авторизации
        try:
            # Ожидаем появление элемента меню пользователя (индикатор успеха)
            WebDriverWait(driver, 15).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-t='profileMenu']"))
            )
            print("\nУспешная авторизация! Элемент меню пользователя обнаружен.")
        except TimeoutException:
            # Проверка альтернативного элемента (если страница изменилась)
            try:
                profile_element = driver.find_element(By.CSS_SELECTOR, "div.UserID")
                self.assertTrue(profile_element.is_displayed(), "Элемент профиля не отображается")
            except NoSuchElementException:
                self.fail("Элементы авторизации не найдены. Тест провален")

    def tearDown(self):
        """Завершение работы после каждого теста"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
