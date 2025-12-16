from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from urls import Urls
from generators import RandomGenerate
from locators import MainPageLocators, AuthPageLocators, RegisterPageLocators


class TestRegistration:
    
    def test_registration_successful(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(RandomGenerate.user_name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(RandomGenerate.email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(RandomGenerate.password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                AuthPageLocators.LOGIN_BUTTON
            )
        )
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(RandomGenerate.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(RandomGenerate.password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == Urls.MAIN_PAGE_URL
        
    def test_registration_unsuccessful(self, driver):
       
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(RandomGenerate.user_name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(RandomGenerate.email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("aaaa")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        error_message = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                RegisterPageLocators.ERROR_MESSAGE
            )
        )
        
        assert error_message.text == 'Некорректный пароль'
        
        
                                                                           
        
        
     