from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")

    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")

    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")

    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")

    METRO_STATION_TEMPLATE = '//button[@data-value="{value}"]'
    METRO_STATION_ALL = (By.XPATH, '//*[@class="select-search__option"]')
    METRO_STATION_VISIBLE = (By.XPATH, '//*[@class="select-search__row" '
                                       'and @role="menuitem"]')

    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")

    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')

    DATE_INPUT = (By.XPATH,
                  './/input[@placeholder="* Когда привезти самокат"]')
    DAY_LOCATOR = (By.XPATH,
                   './/div[contains(@class, "react-datepicker__day--today")]')

    RENTAL_DURATION_DROPDOWN = (By.XPATH,
                                '//div[@class="Dropdown-control"]')
    RENTAL_DURATION_OPTION = (By.XPATH,
                              '//div[@class="Dropdown-menu"]//div[text()="{}"]')

    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")

    COMMENT_INPUT = (By.XPATH,
                     "//input[contains(@placeholder, 'Комментарий')]")

    MAKE_ORDER_BUTTON = (By.XPATH,
                         '//button[contains(@class, "Button_Middle") '
                         'and contains(text(), "Заказать")]')

    ORDER_BUTTON_ALL_SIZES = (By.XPATH,
                              '//div[contains(@class, "Home_FinishButton")]'
                              '/button[contains(@class, "Button_Button") '
                              'and contains(text(), "Заказать")]')

    YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button") '
                            'and contains(text(), "Да")]')

    STATUS_WINDOW = (By.XPATH, '//div[contains(@class,"Order_ModalHeader")]')