from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    TIMEOUT = 5

    # ===Баннер с куками (закрываем в начале каждого теста)=== #
    COOKIE_CONFIRM_BUTTON = (By.ID, 'rcc-confirm-button')

    # ===Шапка=== #
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, text):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        return element.text

    def wait_visibility(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        return element

    def scroll(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def close_cookie_banner(self):
        self.click(self.COOKIE_CONFIRM_BUTTON)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    def switch_to_new_window(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
