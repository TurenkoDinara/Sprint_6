import allure
import pytest
from data.data import Urls, Users
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators

class TestOrderPage:

    @allure.title("Проверка оформления заказа по кнопке 'Заказать' в шапке")
    @allure.description("Способ формы заполнения в отдельном методе. Использую 2 различных набора данных для проверки")
    @pytest.mark.parametrize("entry_point,user", [
        ("top", Users.user_1),
        ("bottom", Users.user_2),
    ])
    def test_order_flow(self, entry_point, user, driver):
        main = MainPage(driver)
        order = OrderPage(driver)

        main.go_to_url(Urls.MAIN_PAGE)

        if entry_point == "top":
            main.accept_cookies()
            main.click_order_top()
            order.order_form_fill_out_on_button_top(user)
        else:
            main.accept_cookies()
            main.click_order_bottom()
            order.order_form_fill_out_on_bottom_button(user)

        assert order.is_order_completed(), "Ожидалось всплывающее окно 'Заказ оформлен'"
