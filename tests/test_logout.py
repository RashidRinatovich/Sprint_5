from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from generators import Person
from urls import Urls
from locators import (
    MainPageLocators,
    AuthPageLocators,
    ProfilePageLocators
)
class TestLogout:
    def test_personal_account_exit(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()
    
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                ProfilePageLocators.EXIT_BUTTON
            )
        ).click()
    
        WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            AuthPageLocators.LOGIN_BUTTON
            )
        )
        assert driver.current_url == Urls.AUTH_PAGE_URL