import allure
from selenium.common import NoSuchElementException, TimeoutException

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import ACCOUNT_URL, BASE_URL


class MainPage(BasePage):
    @allure.step('Перейти на страницу аккаунта')
    def go_to_account_page(self):
        self.go_to_url(ACCOUNT_URL)
        self.wait_for_visible_element(MainPageLocators.CONSTRUCT_HEADER_LINK)

    @allure.step('Перейти на главную страницу')
    def go_to_main_page(self):
        self.go_to_url(BASE_URL)
        self.wait_for_visible_element(MainPageLocators.CONSTRUCT_HEADER_LINK)

    @allure.step('Кликнуть по кнопке Конструктор')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCT_HEADER_LINK)

    @allure.step('Проверить, что вкладка Конструктор отображается')
    def is_constructor_section_visible(self):
        return self.is_element_displayed(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Кликнуть по кнопке Лента заказов')
    def click_on_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверить, что вкладка Лента заказов отображается')
    def is_order_feed_section_visible(self):
        return self.is_element_displayed(MainPageLocators.ORDER_FEED_HEADER)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_N200i_BUN)

    @allure.step('Проверить, отображается всплывающее окно с информацией об ингредиенте')
    def is_ingredients_details_displayed(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
        return element.is_displayed()

    @allure.step('Проверить, всплывающее окно с информацией об ингредиенте закрыто')
    def is_ingredients_details_closed(self):
        try:
            self.wait_for_invisible_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
            return True
        except TimeoutException:
            return False

    @allure.step('Кликнуть по крестику всплывающего окна')
    def click_on_close_details_button(self):
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Скролл до ингредиента "Соус фирменный Space Sauce"')
    def scroll_to_sauce(self):
        self.click_on_element(MainPageLocators.INGREDIENT_FIRM_SAUCE)

    @allure.step('Получить количество ингредиентов в заказе "Соус фирменный Space Sauce"')
    def get_ingredient_count(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_FIRM_SAUCE_COUNTER)


    @allure.step('Кликнуть по кнопке заказать')
    def click_on_make_order_button(self):
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Перетащить соус в корзину')
    def put_sauce_into_basket(self):
        self.is_constructor_section_visible()
        ingredient = self.wait_for_visible_element(locator=MainPageLocators.INGREDIENT_FIRM_SAUCE)
        basket = self.wait_for_visible_element(locator=MainPageLocators.ORDER_TARGET_TOP)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Перетащить булочку в корзину')
    def put_bun_into_basket(self):
        self.is_constructor_section_visible()
        ingredient = self.wait_for_visible_element(locator=MainPageLocators.INGREDIENT_N200i_BUN)
        basket = self.wait_for_visible_element(locator=MainPageLocators.ORDER_TARGET_TOP)
        self.drag_and_drop_element(source=ingredient, target=basket)