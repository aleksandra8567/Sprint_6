import allure
import pytest
from selenium import webdriver
from .data import URLs

@pytest.fixture()
@allure.title("Подготовка драйвера")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--width=1920')
    firefox_options.add_argument('--height=1080')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(URLs.main_page)
    yield driver
    driver.quit()