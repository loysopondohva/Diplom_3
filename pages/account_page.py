import allure

import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import ACCOUNT_URL, BASE_URL


class AccountPage(BasePage):

    @allure.step('Перейти на страницу аккаунта')
    def go_to_account_page(self):
        self.go_to_url(ACCOUNT_URL)
        self.wait_for_visible_element(MainPageLocators.CONSTRUCT_HEADER_LINK)

    @allure.step('Логин в систему')
    def login_to_account(self, email, password):
        self.go_to_account_page()
        self.send_keys_to_input(AccountPageLocators.LOGIN_EMAIL, data.Credentials.email)
        self.send_keys_to_input(AccountPageLocators.LOGIN_PASSWORD, data.Credentials.password)
        self.click_on_element(AccountPageLocators.LOGIN_BUTTON)
        self.wait_for_visible_element(MainPageLocators.CONSTRUCTOR_HEADER)
