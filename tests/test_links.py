import allure
import pytest

from pages.main_page import MainPage
from data.data import Urls
from selenium.webdriver.support.ui import WebDriverWait

class TestLogo:

    @allure.title("Проверка перехода на главную страницу по логотипу 'Самокат'")
    def test_click_scooter_logo_redirects_to_main(self, driver):
        main = MainPage(driver)
        driver.get(Urls.ORDER_PAGE)   # откроем страницу заказа, чтобы проверить переход на главную
        main.click_scooter_logo()
        assert Urls.MAIN_PAGE in driver.current_url

    @allure.title("Проверка перехода на страницу 'Дзена' по клику на логотип 'Яндекс'")
    def test_click_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)
        main.go_to_url(Urls.MAIN_PAGE)
        main.click_yandex_logo()

        # переключаемся на новую вкладку
        handles = driver.window_handles
        if len(handles) > 1:
            driver.switch_to.window(handles[-1])

        # ЯВНОЕ ОЖИДАНИЕ — пока URL изменится с about:blank
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != "about:blank"
        )

        current = driver.current_url.lower()
        assert "dzen" in current or "yandex" in current, f"Ожидали dzen, но получили {current}"
