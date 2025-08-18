import allure
import pytest  # Обязательно импортируем pytest
from helpers.webdriver import WebdriverFactory

# Эта функция добавляет возможность передачи параметра --browser в командной строке pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="Выбор браузера: 'chrome' или 'firefox'."
    )

@pytest.fixture
def driver(request):
    # Получаем параметр браузера из командной строки
    browser_name = request.config.getoption("--browser")
    # Создаем и возвращаем соответствующий драйвер
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()  # Открытие окна на весь экран
    yield driver
    driver.quit()
