import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


"""
Базовый класс для всех Page Object классов
Общая функциональность для работы со страницами
"""



class BasePage:

    def __init__(self, driver):
        self.driver = driver
    # метод перехода на страницу
    @allure.step("Переход на страницу")
    def go_to_url(self, url):
        self.driver.get(url)

    # метод поиска и явного ожидания элемента на странице
    @allure.step("Поиск и явное ожидание элемента")
    def find_and_wait_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # метод клика по элементу
    @allure.step("Клик по элементу")
    def click_on_locator(self, locator):
        self.find_and_wait_locator(locator).click()

    # метод ожидания появления элемента на странице
    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # метод получения текста
    @allure.step("Получение текста элемента")
    def get_text (self, locator):
        return self.find_and_wait_locator(locator).text

    # метод скрола до элемента на странице
    @allure.step("Скрол до элемента")
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод заполнения формы на странице
    @allure.step("Ввод данных в поле")
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)