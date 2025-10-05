from selenium.webdriver.common.by import By


class OrderPageLocators:
    # ФОРМА ЗАКАЗА САМОКАТА
    # Локатор для поля "Имя"
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    # Локатор для поля "Фамилия"
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # Локатор для поля "Адрес"
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # Локатор для поля "Станция метро"
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # Локатор для станции "Сокольники"
    METRO_STATION_1 = (By.XPATH, '//div[text() = "Сокольники"]')
    # Локатор для станции "Комсомольская"
    METRO_STATION_2 = (By.XPATH, '//div[text() = "Комсомольская"]')
    # Локатор для поля "Телефон"
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    # Локатор кнопки "Далее"
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')

    # ЛОКАТОРЫ БЛОКА "ПРО АРЕНДУ"
    # Локатор для поля "Когда привезти самокат"
    DATA_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    # Локатор для поля "Срок аренды"
    RENT_FIELD = (By.XPATH, './/div[text()="* Срок аренды"]')
    #Локатор для цвета "Черный жемчуг"
    BLACK_CHEK_BOX = (By.ID, 'black')
    # Локатор для цвета "Черный жемчуг"
    GREY_CHEK_BOX = (By.ID, 'grey')
    # Локатор для поля "Комментарий для курьера"
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Локатор для выбранной даты в календаре
    SELECTED_DATE = (By.XPATH, '//div[@aria-label="Choose среда, 1-е октября 2025 г."]')
    # Локатор для срока "Сутки"
    SELECTED_RENT = (By.XPATH, './/div[text()="сутки"]')

    # Локатор для кнопки "Заказать"
    ORDER_BUTTON = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")

    # ЛОКАТОРЫ БЛОКА "Хотите оформить заказ?"
    # Локатор для кнопки "Да"
    YES_BUTTON = (By.XPATH, './/button[text()="Да"]')
    # Локатор для кнопки "Нет"
    NO_BUTTON = (By.XPATH, './/button[text()="Нет"]')

    # Локатор на всплывающее окно о подтверждении заказа
    # Локатор на тест "Заказ оформлен"
    ORDER_COMPLETED = (By.XPATH, './/div[text()="Заказ оформлен"]')
    # Локатор на кнопку "Посмотреть статус"
    VIEW_STATUS_BUTTON = (By.XPATH, './/div[text()="Посмотреть статус"]')

    # Локатор логотипа "Самоката"
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")
    # Локатор логотипа "Яндекс"
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")

