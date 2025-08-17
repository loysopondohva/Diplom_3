from selenium.webdriver.common.by import By

# Локаторы для главной страницы
class MainPageLocators:

    # Кнопка Конструктор
    CONSTRUCT_HEADER_LINK   = (By.XPATH, "//header/nav//a//p[contains(text(), 'Конструктор')]")
    # Заголовок Конструктора для проверки перехода
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    MAKE_ORDER_BUTTON = (By.XPATH, "//main//button[contains(text(), 'Оформить заказ')]")
    ACCOUNT_HEADER_LINK = (By.XPATH, "//header//a//p[contains(text(), 'Личный Кабинет')]")

    # Кнопка Лента Заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    # Заголовок Лента Заказов для проверки перехода
    ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")

    # Ингредиент "Краторная булка N-200i"
    INGREDIENT_N200i_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']")

    # Ингредиент "Соус фирменный Space Sauce"
    INGREDIENT_FIRM_SAUCE = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']")

    # Заголовок с деталями ингредиента при клике на булку
    INGREDIENT_DETAILS_TITLE = (By.XPATH,
                                "//h2[contains(text(),'Детали ингредиента')]")

    # Крестик для закрытия деталей ингредиента
    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH,
          "//div[contains(@class,'modal__container')]//button[contains(@class,'modal__close')]")

    ORDER_TARGET_TOP = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    # Ингредиент "Соус фирменный Space Sauce"
    INGREDIENT_FIRM_SAUCE_COUNTER = (By.XPATH, "//img[@alt='Соус фирменный Space Sauce']/preceding-sibling::div/p")

    INGREDIENT_COUNTER = (By.XPATH, "//img[@alt='Краторная булка N-200i']/preceding-sibling::div/p")

