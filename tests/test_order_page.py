from pages.order_page import OrderPageScooter
from pages.main_page import MainPageScooter
from data import DataSet

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import urls
import pytest
import allure


class TestPositiveScenario:

    @allure.title('Проверка позитивного сценария заказа, точка входа: {entry_name}')
    @pytest.mark.parametrize('entry_point, entry_name, user_data', [
        ('top', 'кнопка «Заказать» в шапке', DataSet.ORDER_DATA_SET_1),
        ('bottom', 'кнопка «Заказать» в нижней части страницы', DataSet.ORDER_DATA_SET_2)])
    def test_order_success_2_buttons(self, driver, entry_point, entry_name, user_data):
        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)

        main_page.load_main_page()
        main_page.close_cookie_banner()

        if entry_point == 'top':
            main_page.order_button_top_click()
        else:
            main_page.scroll_to_order_button_bottom()
            main_page.order_button_bottom_click()

        order_page.fill_personal_data(**user_data['For_Whom'])
        order_page.click_next_button()
        order_page.fill_order_data(**user_data['About_Order'])
        order_page.click_order_button()
        order_page.confirm_order()

        assert 'Заказ оформлен' in order_page.get_success_modal_header_text()


class TestRedirects:

    @allure.title('Проверка редиректа на Дзен при нажатии на Яндекс Лого в шапке')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        order_page = OrderPageScooter(driver)

        order_page.load_order_page()
        order_page.close_cookie_banner()
        order_page.click_yandex_logo()
        order_page.switch_to_new_window()

        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url

    @allure.title('Проверка редиректа на главную при нажатии на "Самокат" в шапке')
    def test_click_scooter_redirects_to_main(self, driver):
        order_page = OrderPageScooter(driver)

        order_page.load_order_page()
        order_page.close_cookie_banner()
        order_page.click_scooter_logo()

        assert WebDriverWait(driver, 5).until(EC.url_to_be(urls.MAIN_PAGE_URL))
