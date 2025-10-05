from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

"""
Класс главной страницы сайта, наследуемый от Base_Page
"""



class MainPage(BasePage):
    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_order_top(self):
        self.click_on_locator(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_order_bottom(self):
        self.scroll_to_locator(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_locator(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Принятие куки")
    def accept_cookies(self):
        try:
            self.click_on_locator(MainPageLocators.COOKIES_BUTTON)
        except Exception:
            # если баннера нет — просто продолжаем
            pass

    @allure.step("Клик по вопросу №{index}")
    def click_question(self, index):
        questions = [
            MainPageLocators.QUESTION_1, MainPageLocators.QUESTION_2, MainPageLocators.QUESTION_3, MainPageLocators.QUESTION_4,
            MainPageLocators.QUESTION_5, MainPageLocators.QUESTION_6, MainPageLocators.QUESTION_7, MainPageLocators.QUESTION_8
        ]
        self.scroll_to_locator(questions[index])
        self.click_on_locator(questions[index])

    @allure.step("Получение текста ответа на вопрос №{index}")
    def get_answer_text(self, index):
        answers = [
            MainPageLocators.ANSWER_1, MainPageLocators.ANSWER_2, MainPageLocators.ANSWER_3, MainPageLocators.ANSWER_4,
            MainPageLocators.ANSWER_5, MainPageLocators.ANSWER_6, MainPageLocators.ANSWER_7, MainPageLocators.ANSWER_8
        ]
        return self.get_text(answers[index])

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_locator(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_locator(OrderPageLocators.YANDEX_LOGO)