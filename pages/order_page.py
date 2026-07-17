from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

import urls


class OrderPageScooter(BasePage):

    # ===Форма заказа, ОКНО 1 «Для кого самокат»=== #
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Станция метро: клик по полю раскрывает список, далее выбор — по тексту станции (оставить дырку для функции)
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_OPTION = ".//div[@class='select-search__select']//div[text()='{}']"

    @staticmethod
    def metro_option(station_name):
        return (By.XPATH, OrderPageScooter.METRO_OPTION.format(station_name))

    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # ===Форма заказа, ОКНО 2 «Про аренду»=== #
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")

    # Срок аренды: выпадающий лист, далее выбор — по тексту опции (оставить дырку для функции)
    RENT_PERIOD_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    RENT_PERIOD_OPTION = ".//div[@class='Dropdown-option' and text()='{}']"

    @staticmethod
    def rent_period_option(period):
        return (By.XPATH, OrderPageScooter.RENT_PERIOD_OPTION.format(period))

    # Цвет самоката
    COLOR_BLACK_CHECKBOX = (By.ID, 'black')   # чёрный жемчуг
    COLOR_GREY_CHECKBOX = (By.ID, 'grey')     # серая безысходность

    COLOR_CHECKBOXES = {
        'black': COLOR_BLACK_CHECKBOX,
        'grey': COLOR_GREY_CHECKBOX}

    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    # Промежуточно ищем вхожение Order_Buttons, так как 2 кнопки на странице:
    # просто text()='Заказать' найдёт две кнопки. АТТЕНШН!
    ORDER_BUTTON = (
        By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    BACK_BUTTON = (
        By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Назад']")

    # ===Модалка подтверждения «Хотите оформить заказ?»=== #
    CONFIRM_YES_BUTTON = (
        By.XPATH, ".//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    CONFIRM_NO_BUTTON = (
        By.XPATH, ".//div[contains(@class, 'Order_Modal')]//button[text()='Нет']")

    # ===Модалка успеха=== #
    # Заголовок содержит: «Заказ оформлен. Номер заказа: 123456…»,
    # поэтому проверять текст вхождением
    SUCCESS_MODAL_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")
    STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    # Пиши-сокращай для тестов :) Хи хи.
    # Прописываем методы, чтобы к ним обращаться из теста, и не светить там локаторы:

    def load_order_page(self):
        self.driver.get(urls.ORDER_PAGE_URL)

    def choose_color(self, color):
        self.click(self.COLOR_CHECKBOXES[color])

    def fill_personal_data(self, name, surname, address, metro, phone):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.SURNAME_INPUT, surname)
        self.fill(self.ADDRESS_INPUT, address)
        self.click(self.METRO_INPUT)
        self.click(self.metro_option(metro))
        self.fill(self.PHONE_INPUT, phone)

    def fill_order_data(self, date, period, color, comment):
        self.fill(self.DATE_INPUT, date)
        self.wait_visibility(self.DATE_INPUT).send_keys(Keys.ESCAPE)
        self.click(self.RENT_PERIOD_DROPDOWN)
        self.click(self.rent_period_option(period))
        self.choose_color(color)
        self.fill(self.COMMENT_INPUT, comment)

    def click_next_button(self):
        self.click(self.NEXT_BUTTON)

    def click_order_button(self):
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click(self.CONFIRM_YES_BUTTON)

    def get_success_modal_header_text(self):
        return self.get_text(self.SUCCESS_MODAL_HEADER)
