import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPages: # Название тестового класса

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_open_login_page(self): # Тест пройдет
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"

    def test_open_books_page(self): # Тест упадет
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "qwe", "Ошибка"

    def test_open_profile_page(self): # Тест упадет
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка"

    def teardown(self):
        self.driver.close()