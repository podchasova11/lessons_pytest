import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestExample:


    ABOUT = ("xpath", "//a[text()='About']")

    def setap(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://qaplayground.dev/apps/links/about")
        assert driver.title == "", ""

    @pytest.mark.parametrrize(
        "button,title", [
            (ABOUT, "Welcome to the About Page")
        ]
    )
    def teardown(self):
        self.driver.quit()

