import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data.data import Users


"""
Класс страницы заказа самоката, наследуемый от Base_Page
"""
class OrderPage(BasePage):
    @allure.step("Заполнить поле 'Имя'")
    def set_name(self, name):
        self.send_keys_to_field(OrderPageLocators.NAME_FIELD, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_last_name(self, last_name):
        self.send_keys_to_field(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.send_keys_to_field(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Заполнить поле 'Станция метро'")
    def set_metro(self, metro):
        self.click_on_locator(OrderPageLocators.METRO_FIELD)
        self.send_keys_to_field(OrderPageLocators.METRO_FIELD, metro)
        self.click_on_locator(OrderPageLocators.METRO_STATION_1)


    @allure.step("Заполнить поле 'Телефон'")
    def set_phone(self, phone):
        self.send_keys_to_field(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Клик на кнопку Далее")
    def click_next_button(self):
        self.click_on_locator(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор даты")
    def set_date(self):
        self.click_on_locator(OrderPageLocators.DATA_FIELD)
        self.click_on_locator(OrderPageLocators.SELECTED_DATE)

    @allure.step("Выбор срока аренды")
    def set_rent_duration(self):
        self.click_on_locator(OrderPageLocators.RENT_FIELD)
        self.click_on_locator(OrderPageLocators.SELECTED_RENT)

    @allure.step("Выбор цвета самоката 'Черный'")
    def set_color_black(self):
        self.click_on_locator(OrderPageLocators.BLACK_CHEK_BOX)

    @allure.step("Выбор цвета самоката 'Серый'")
    def set_color_grey(self):
        self.click_on_locator(OrderPageLocators.GREY_CHEK_BOX)

    @allure.step("Ввод комментария: {comment}")
    def set_comment(self, comment):
        self.send_keys_to_field(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Клик на кнопку 'Заказать'")
    def click_order_button(self):
        self.click_on_locator(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click_on_locator(OrderPageLocators.YES_BUTTON)

    @allure.step("Проверка, что заказ оформлен")
    def is_order_completed(self):
        return self.find_and_wait_locator(OrderPageLocators.ORDER_COMPLETED).is_displayed()

    @allure.step("Клик по логотипу 'Самокат'")
    def click_logo_scooter(self):
        self.click_on_locator(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_logo_yandex(self):
        self.click_on_locator(OrderPageLocators.YANDEX_LOGO)

    @allure.step('Заполнение формы и заказ самоката с шапки страницы')
    def order_form_fill_out_on_button_top(self, user_1):
        self.set_name(user_1[0])  # Заполнить Имя
        self.set_last_name(user_1[1])  # Заполнить фамилию
        self.set_address(user_1[2])  # Заполнить адрес
        self.set_metro(user_1[3])  # Заполнить станцию метро
        self.set_phone(user_1[4])  # Заполнить поле Телефон
        self.click_next_button()  # Клик на кнопку Далее
        self.set_date()  # Выбор даты
        self.set_rent_duration()  # Выбор срока аренды
        self.set_color_black()  # Выбор черного самоката
        self.set_comment(user_1[5])  # Ввод комментария
        self.click_order_button()  # Клик на кнопку 'Заказать'
        self.confirm_order()  # Подтверждение заказа


    @allure.step('Заполнение формы и заказ самоката внизу страницы')
    def order_form_fill_out_on_bottom_button(self, user_2):
        self.set_name(user_2[0])  # Заполнить Имя
        self.set_last_name(user_2[1])  # Заполнить фамилию
        self.set_address(user_2[2])  # Заполнить адрес
        self.set_metro(user_2[3])  # Заполнить станцию метро
        self.set_phone(user_2[4])  # Заполнить поле Телефон
        self.click_next_button()  # Клик на кнопку Далее
        self.set_date()  # Выбор даты
        self.set_rent_duration()  # Выбор срока аренды
        self.set_color_grey()  # Выбор серого самоката
        self.set_comment(user_2[5])  # Ввод комментария
        self.click_order_button()  # Клик на кнопку 'Заказать'
        self.confirm_order()  # Подтверждение заказа

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_locator(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_locator(OrderPageLocators.YANDEX_LOGO)