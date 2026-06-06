import allure
from data import URLs
from pages.header_footer_page import HeaderFooterPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.suite('Тестирование переходов с логотипа')
class TestRedirects:

    @allure.title('Проверка перехода по логотипу Самоката')
    @allure.description('Переход на главную страницу Самоката при клике на слово Самокат в логотипе')
    def test_redirect_scooter_logo(self, driver):
        header_footer_page = HeaderFooterPage(driver)
        current_url = header_footer_page.click_scooter_logo()

        assert URLs.main_page in current_url, "Переход на главную страницу Самоката не выполнен"

    @allure.title('Проверка перехода по логотипу Яндекса')
    @allure.description('Переход на главную страницу Дзена при клике на слово Яндекс в логотипе')
    def test_redirect_yandex_logo(self, driver):
        header_footer_page = HeaderFooterPage(driver)
        header_footer_page.go_to_yandex_from_logo()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "your-dzen-logo-selector"))
        )

        current_url = header_footer_page.current_url
        assert URLs.dzen_page in current_url, "Переход на главную страницу Дзена не выполнен"

        is_dzen_logo_displayed = header_footer_page.is_dzen_logo_displayed()
        assert is_dzen_logo_displayed, "Логотип Дзена не найден на странице"