from selenium.webdriver.common.by import By

class AccountPageLocators:

    ACCOUNT_LOGIN_BUTTON = (By.XPATH, "//main//button[contains(text(), 'Войти в аккаунт')]")
    LOGIN_EMAIL = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    LOGIN_PASSWORD = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")
    LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, 'Auth_form')]//button[contains(text(), 'Войти')]")

    # Локаторы для теста выхода из личного кабинета
    ACCOUNT_LOGOUT_BUTTON = (By.XPATH, "//nav//button[contains(text(), 'Выход')]")

    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")  # Кнопка "История заказов"
    ORDER_COMPLETED = (By.XPATH, "//p[contains(text(),'Выполнен')]")  # Выполненные заказы в "Историях заказов"
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]") # Локатор успешного выхода из личного кабинет, кнопка "Вход"
    LOGIN_AFTER_LOGOUT_BURGER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]") # Локатор успешной авторизации


