import allure
from selenium import webdriver

# Подключает webdriver в зависимости от пришедшего параметра
class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            with allure.step('Запускаем браузер Firefox'):
                return webdriver.Firefox()
        elif browser_name == "chrome":
            with allure.step('Запускаем браузер Chrome'):
                return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
