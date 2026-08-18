from pages.main_page import MainPageScooter
from data import FAQSet

import pytest
import allure


class TestFAQ:

    # для ревьюера: question используется в тайтле для репорта.
    # Так как репорты могут читать люди без технических навыков. *ВОТ ЗДЕСЬ:
    @allure.title('Проверка соответствия ответа на вопрос: "{faq_item[question]}" - ожидаемому ответу')
    @pytest.mark.parametrize("index, faq_item", FAQSet.FAQ_DATA_SET.items())
    def test_FAQ_correct_answers(self, driver, index, faq_item):
        main_page = MainPageScooter(driver)

        main_page.load_main_page()
        main_page.close_cookie_banner()
        main_page.scroll_to_FAQ_question(index)
        main_page.click_faq_question(index)
        actual_answer = main_page.get_FAQ_answer_text(index)

        assert actual_answer == faq_item['answer']
