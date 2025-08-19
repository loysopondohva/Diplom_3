from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    MAKE_ORDER_BUTTON = (By.XPATH, "//main//button[contains(text(), 'Оформить заказ')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//header//a//p[contains(text(),'Лента Заказов')]")
    # Заголовок Лента Заказов для проверки перехода
    ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//header//a//p[contains(text(),'Конструктор')]")
    # Заголовок Конструктора для проверки перехода
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    ACCOUNT_HEADER_LINK = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")  # Кнопка "Личный кабинет"

    # Последний заказ в ленте
    LAST_ORDER = ( By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]/a/div")

    # Счётчик "за всё время" (должен увеличиваться при создании заказа)
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//div[@class='OrderFeed_ordersData__1L6Iv']//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p"
    )

    # Счётчик "Выполнено за сегодня" (должен увеличиваться при создании заказа)
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//div[@class='OrderFeed_ordersData__1L6Iv']//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p"
    )

    # Кнопка закрытия окна при заказе
    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")

    # Номер заказа в окне заказа
    ORDER_ID_IN_ORDER_WINDOW = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")

    # Список заказов "В работе"
    ORDER_IN_PROGRESS_LOCATOR = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]")

    # Список заказов "В работе"
    ORDER_IN_ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[contains(@class,'text_type_digits')]")

    # Заголовок Лента заказов или Конструктор
    FEED_TITLE = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")

    ORDER_LOADING_MODAL = (
    By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")

    SECTION_MODAL_INVISIBLE = (By.XPATH,"//section[contains(@class,'Modal_modal__P3_V5')]")
    DIV_MODAL_INVISIBLE = (By.XPATH,"//div[contains(@class,'Modal_modal__P3_V5')]")


