import allure
import data
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage


@allure.feature('Основной функционал')
@allure.story('Тесты раздела Ленты заказов')
class TestOrderFeedPage:
    @allure.title('Тест увеличения счётчика "Выполнено за всё время" при создании заказа')
    def test_increase_count_total_orders(self, driver):

        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        with allure.step('Логинимся в системе'):
            user_email = data.Credentials.email
            user_password = data.Credentials.password
            account_page.login_to_account(user_email, user_password)
        with allure.step('Переходим в ленту заказов'):
            order_feed_page.click_to_order_feed_button()

        with allure.step('Запоминаем количество заказов в счётчике "Выполнено за всё время"'):
            orders_count_before = order_feed_page.get_total_orders_count()

        with allure.step('Создаём заказа'):
            order_feed_page.click_to_constructor_button()
            main_page.put_bun_into_basket()
            main_page.put_sauce_into_basket()
            order_feed_page.click_to_make_order_button()

        with allure.step('Закрываем окно с деталями заказа'):
            order_feed_page.wait_and_get_order_number()
            order_feed_page.click_to_close_order_details_button()

        with allure.step('Переходим в ленту заказов'):
            order_feed_page.click_to_order_feed_button()

        with allure.step('Смотрим количество заказов в счётчике "Выполнено за всё время"'):
            orders_count_after = order_feed_page.get_total_orders_count()

        with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
            assert orders_count_after > orders_count_before, \
                f"Ожидалось увеличение счетчика на 1. Было: {orders_count_before}, стало: {orders_count_after}"

    @allure.title('Тест увеличения счётчика "Выполнено за сегодня" при создании заказа')
    def test_increase_count_today_orders(self, driver):

        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        with allure.step('Логинимся в системе'):
            user_email = data.Credentials.email
            user_password = data.Credentials.password
            account_page.login_to_account(user_email, user_password)
        with allure.step('Переходим в ленту заказов'):
            order_feed_page.click_to_order_feed_button()

        with allure.step('Запоминаем количество заказов в счётчике "Выполнено за сегодня"'):
            orders_count_before = order_feed_page.get_today_orders_count()

        with allure.step('Создаём заказ'):
            order_feed_page.click_to_constructor_button()
            main_page.put_bun_into_basket()
            main_page.put_sauce_into_basket()
            order_feed_page.click_to_make_order_button()

        with allure.step('Закрываем окно с деталями заказа'):
            order_feed_page.wait_and_get_order_number()
            order_feed_page.click_to_close_order_details_button()

        with allure.step('Переходим в ленту заказов'):
            order_feed_page.click_to_order_feed_button()

        with allure.step('Смотрим количество заказов в счётчике "Выполнено за сегодня"'):
            orders_count_after = order_feed_page.get_today_orders_count()

        with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
            assert orders_count_after > orders_count_before, \
                f"Ожидалось увеличение счетчика на 1. Было: {orders_count_before}, стало: {orders_count_after}"

    @allure.title('Тест появления номера заказа в списке "В работе" при создании заказа')
    def test_order_id_in_orders_in_progress(self, driver):
        account_page = AccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        with allure.step('Логинимся в системе'):
            user_email = data.Credentials.email
            user_password = data.Credentials.password
            account_page.login_to_account(user_email, user_password)
        with allure.step('Создаём заказа'):
            order_feed_page.click_to_constructor_button()
            main_page.put_bun_into_basket()
            main_page.put_sauce_into_basket()
            order_feed_page.click_to_make_order_button()

        with allure.step('Закрываем окно с деталями заказа'):
            order_id = order_feed_page.wait_and_get_order_number()
            order_feed_page.click_to_close_order_details_button()

        with allure.step('Переходим в ленту заказов'):
             order_feed_page.click_to_order_feed_button()

        with allure.step('Смотрим номер заказа в разделе "В Работе"'):
            order_id_in_progress = order_feed_page.get_order_id_in_progress()

        with allure.step('Проверяем, номер заказа в разделе "В работе" совпадает с нашим номером заказа'):
             assert order_id == order_id_in_progress , \
                 f"Ожидалось номер заказа: {order_id} в разделе 'В работе', Номер заказа в разделе: {order_id_in_progress}"

