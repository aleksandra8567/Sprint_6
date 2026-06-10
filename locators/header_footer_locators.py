from selenium.webdriver.common.by import By

class HeaderFooterLocators:

    COOKIE_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button" and '
                               'contains(@class, "App_CookieButton")]')

    YANDEX_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoYandex')]")

    SAMOKAT_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoScooter')]")

    DZEN_LOGO = (By.XPATH, '//a[@aria-label="Логотип Бренда"]')