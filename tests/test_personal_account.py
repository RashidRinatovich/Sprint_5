from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from generators import Person, RandomGenerate
from urls import Urls
from locators import (
    MainPageLocators,
    AuthPageLocators,
    ProfilePageLocators
)

class TestPersonalAccount:
    def test_crossing_personal_account_button(self, driver):
    
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
    
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                AuthPageLocators.LOGIN_BUTTON
            )
        ).click()
    
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()
        
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ProfilePageLocators.PROFILE_LINK
            )
        )
        assert driver.current_url == Urls.PERSONAL_ACCOUNT_PAGE_URL
    
    def test_crossing_personal_account_constructor_button(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
    
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                AuthPageLocators.LOGIN_BUTTON
            )
        ).click()
    
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()
    
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ProfilePageLocators.CONSTRUCTOR_BUTTON
            )
        ).click()
    
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                 MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == Urls.MAIN_PAGE_URL   
        
    def test_crossing_personal_account_constructor_logo(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(RandomGenerate.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(RandomGenerate.password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                AuthPageLocators.LOGIN_BUTTON
            )
        ).click()
        
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ). click()
        
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(
                ProfilePageLocators.LOGO_LINK
            )
        ). click()
        
        assert driver.current_url == Urls.MAIN_PAGE_URL
        
