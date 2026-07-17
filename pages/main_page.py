from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import urls


class MainPageScooter(BasePage):

    # Кнопка «Заказать» в шапке
    # Промежуточно ищем вхожение по классу хедера, так как 2 кнопки на странице:
    # просто text()='Заказать' найдёт две кнопки. АТТЕНШН!
    ORDER_BUTTON_TOP = (
        By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")

    # Кнопка «Заказать» внизу страницы
    ORDER_BUTTON_BOTTOM = (
        By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # ===Раздел «Вопросы о важном» (FAQ)=== #
    # У гармошек уникальные id: accordion__heading-0 (*от 0 до 7)
    # а у панели ответов accordion__panel-0 (*от 0 до 7)
    # 16 раз писать  - долго, оставляем общее и дырку под функцию.

    FAQ_QUESTION = 'accordion__heading-{}'
    FAQ_ANSWER = 'accordion__panel-{}'  # -> шаблоны + параметризация вместо 16 констант.

    # Функция выбора вопроса — по индексу, и одна для проверки ответа по индексу.
    # *использовать в тестах через параметризацию
    @staticmethod
    def faq_question(index):
        return (By.ID, MainPageScooter.FAQ_QUESTION.format(index))

    @staticmethod
    def faq_answer(index):
        return (By.ID, MainPageScooter.FAQ_ANSWER.format(index))

    # Прописываем методы, чтобы к ним обращаться из теста, и не светить там локаторы:
    def load_main_page(self):
        self.driver.get(urls.MAIN_PAGE_URL)

    def order_button_top_click(self):
        self.click(self.ORDER_BUTTON_TOP)

    def order_button_bottom_click(self):
        self.click(self.ORDER_BUTTON_BOTTOM)

    def scroll_to_order_button_bottom(self):
        self.scroll(self.ORDER_BUTTON_BOTTOM)

    def scroll_to_FAQ_question(self, index):
        self.scroll(self.faq_question(index))

    def click_faq_question(self, index):
        self.click(self.faq_question(index))

    def get_FAQ_answer_text(self, index):
        return self.get_text(self.faq_answer(index))
