from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{0}']")

    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains('
                                     '@class, "Button_Button") and contains('
                                     'text(), "Заказать")]')

    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class,'
                                     ' "Button_Button") and contains('
                                     '@class, "Button_Middle") and contains('
                                     'text(), "Заказать")]')