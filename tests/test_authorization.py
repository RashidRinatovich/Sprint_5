from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from generators import Person
from urls import Urls
from locators import MainPageLocators, AuthPageLocators, RegisterPageLocators, RecoveryPageLocators


class TestAuthorization:
    def test_enter_login_account_button(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == Urls.MAIN_PAGE_URL
        
        
    def test_enter_button_personal_account(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert order_button.text == 'Оформить заказ'
        
    def test_enter_button_login_page(self, driver):
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert order_button.text == 'Оформить заказ'
        
        
    def test_button_enter_password_recovery(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.RECOVER_LINK).click()
        driver.find_element(*RecoveryPageLocators.LOGIN_LINK).click()
        
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert order_button.text == 'Оформить заказ'