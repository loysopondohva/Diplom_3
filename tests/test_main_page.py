import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
# from pages.account_page import AccountPage
from data import Credentials
import time

@allure.feature('Основной функционал')
@allure.story('Тесты функционала главной страницы')
class TestMainPage:

    @allure.title('Тест перехода в конструктор')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.go_to_account_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_on_constructor_button()

        with allure.step('Проверяем, что секция "Собери бургер" отображается'):
           assert main_page.is_constructor_section_visible(), "Секция 'Собери бургер' не отображается!"

    @allure.title('Тест перехода в Ленту заказов')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.go_to_account_page()

        with allure.step('Нажимаем на "Ленту заказов"'):
            main_page.click_on_order_feed_button()

        with allure.step('Проверяем, что секция "Лента заказов"'):
           assert main_page.is_order_feed_section_visible(), "Секция 'Лента заказов' не отображается!"


    @allure.title('Тест появления всплывающего окна с деталями при клике по ингредиенту')
    def test_click_ingredient_open_details(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.go_to_main_page()

        with allure.step('Нажимаем на ингредиент "Краторная булка N-200i"'):
            main_page.click_on_ingredient()

        with allure.step('Проверяем, что отображается всплывающее окно'):
           assert main_page.is_ingredients_details_displayed(), "Всплывающее окно с деталями ингредиентами не отображается"

    @allure.title('Тест закрытия всплывающего окна с деталями при клике по ингредиенту')
    def test_click_close_details_button_close_details(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.go_to_main_page()

        with allure.step('Нажимаем на ингредиент "Краторная булка N-200i"'):
            main_page.click_on_ingredient()

        with allure.step('Нажимаем на крестик на всплывющем окне"'):
            main_page.click_on_close_details_button()

        with (allure.step('Проверяем, что не отображается всплывающее окно')):
           assert main_page.is_ingredients_details_closed(), \
                "Всплывающее окно с деталями ингредиента отображается"

    @allure.title('Тест что добавлении ингредиента в заказ, его счётчик увеличивается')
    def test_increase_ingredient_count(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.go_to_main_page()

        with allure.step('Получаем количество соусов до добавления'):
            count_before = main_page.get_ingredient_count()

        with allure.step('Добавляем соус в корзину'):
            main_page.put_sauce_into_basket()

        with allure.step('Получаем количество соусов после добавления'):
            count_after = main_page.get_ingredient_count()

        with (allure.step('Проверяем, количество в заказе увеличилось')):
           assert count_after > count_before, \
                "Всплывающее окно с деталями ингредиента отображается"
