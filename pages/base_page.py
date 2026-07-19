from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import urls
import allure


class BasePage:

    TIMEOUT = 5

    # ===Баннер с куками (закрываем в начале каждого теста)=== #
    COOKIE_CONFIRM_BUTTON = (By.ID, 'rcc-confirm-button')

    # ===Шапка=== #
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Открываем главную страницу')
    def load_main_page(self):
        self.open_page(urls.MAIN_PAGE_URL)

    @allure.step('Открываем страницу заказа')
    def load_order_page(self):
        self.open_page(urls.ORDER_PAGE_URL)

    @allure.step('Кликаем на элемент по локатору: "{locator}"')
    def click(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Заполняем поле элемента по локатору: "{locator}" текстом "{text}"')
    def fill(self, locator, text):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step('Получаем текст элемента по локатору: "{locator}"')
    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        return element.text

    @allure.step('Ждём видимость элемента по локатору: "{locator}"')
    def wait_visibility(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        return element

    @allure.step('Скроллим до элемента по локатору: "{locator}"')
    def scroll(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Закрываем куки баннер')
    def close_cookie_banner(self):
        self.click(self.COOKIE_CONFIRM_BUTTON)

    @allure.step('КЛикаем на слово "Самокат" в шапке')
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step('Кликаем на лого Яндекса в шапке')
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step('Переключаемся на открывшееся окно')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ждём, пока URL станет "{url}"')
    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.url_to_be(url))

    @allure.step('Ждём, пока URL будет содержать "{text}"')
    def wait_url_contains(self, text):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.url_contains(text))
