from pages.main_page import MainPageScooter
from data import FAQSet

import pytest


class TestFAQ:

    @pytest.mark.parametrize("index, expected_answer", FAQSet.FAQ_DATA_SET.items())
    def test_FAQ_correct_answers(self, driver, index, expected_answer):
        main_page = MainPageScooter(driver)

        main_page.load_main_page()
        main_page.close_cookie_banner()
        main_page.scroll_to_FAQ_question(index)
        main_page.click_faq_question(index)
        actual_answer = main_page.get_FAQ_answer_text(index)

        assert actual_answer == expected_answer
