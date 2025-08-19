import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_visible_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Подождать невидимости элемента")
    def wait_for_invisible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))


    @allure.step("Подождать присутствия элемента")
    def wait_for_presence_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        return element.text

    @allure.step("Получить атрибут элемента")
    def get_element_attribute(self, locator, attribute_name, timeout=10):
        element = self.wait_for_presence_element(locator, timeout)
        return element.get_attribute(attribute_name)

    @allure.step("Получить CSS свойство элемента")
    def get_element_css_property(self, locator, property_name, timeout=10):
        element = self.wait_for_presence_element(locator, timeout)
        return element.value_of_css_property(property_name)

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Перейти на другую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получить текущий url страницы")
    def get_page_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Проверить отображение элемента')
    def is_element_displayed(self, locator):
        try:
            element = self.wait_for_visible_element(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step('Перейти на страницу')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Подождать пока изменится текст на элементе')
    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda _: self.get_text_on_element(locator) != initial_text, timeout
        )
        return self.wait_for_visible_element(locator)