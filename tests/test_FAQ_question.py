import allure
import pytest
from data.data import Urls, FAQ_ANSWERS
from pages.main_page import MainPage

class TestMainPage:
    @allure.title("Проверка блока с вопросами")
    @allure.description("При нажатии на вопрос открывается ответ")
    @pytest.mark.parametrize("index, expected_text", list(enumerate(FAQ_ANSWERS)))
    def test_faq_answers(self, driver, index, expected_text):
        page = MainPage(driver)
        page.go_to_url(Urls.MAIN_PAGE)
        page.click_question(index)
        answer = page.get_answer_text(index)
        assert expected_text in answer