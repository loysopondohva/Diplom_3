import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть на ленту заказов')
    def click_to_order_feed_button(self):
        self.wait_for_invisible_element(OrderFeedPageLocators.SECTION_MODAL_INVISIBLE)
        self.wait_for_invisible_element(OrderFeedPageLocators.DIV_MODAL_INVISIBLE)
        self.wait_for_visible_element(OrderFeedPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(OrderFeedPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_visible_element(OrderFeedPageLocators.ORDER_FEED_HEADER)

    @allure.step('Кликнуть на конструктор заказов')
    def click_to_constructor_button(self):
        self.wait_for_invisible_element(OrderFeedPageLocators.SECTION_MODAL_INVISIBLE)
        self.wait_for_invisible_element(OrderFeedPageLocators.DIV_MODAL_INVISIBLE)
        self.wait_for_visible_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_visible_element(OrderFeedPageLocators.CONSTRUCTOR_HEADER)


    @allure.step('Посмотреть количество заказов')
    def get_total_orders_count(self):
        count = self.get_text_on_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        return count

    @allure.step('Посмотреть количество заказов за сегодня')
    def get_today_orders_count(self):
        count = self.get_text_on_element(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)
        return count

    def is_order_number_in_progress(self, order_id):
        self.wait_for_visible_element(OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR)
        order_id_in_progress = self.get_text_on_element(OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR)
        return order_id in order_id_in_progress

    def get_order_id_in_progress(self):
        order_id_in_progress = self.get_text_on_element(OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR)
        return order_id_in_progress

    @allure.step('Кликнуть по кнопке заказать')
    def click_to_make_order_button(self):
        self.click_on_element(OrderFeedPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Кликнуть по кнопке закрытия окна заказа')
    def click_to_close_order_details_button(self):
        self.click_on_element(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)


    @allure.step('Дождаться и посмотреть номер заказа')
    def wait_and_get_order_number(self):
        order_id_element = self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID_IN_ORDER_WINDOW,'9999')
        order_id = f"{int(order_id_element.text):07d}" # Дополняем order_id нулями

        return order_id
