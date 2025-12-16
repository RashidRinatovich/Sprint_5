from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver import ActionChains
from locators import BurgerIngredientLocators
 
class TestConstructor:
    
    @pytest.mark.parametrize("tab_locator, section_locator, expected_text", [
        (BurgerIngredientLocators.BUNS_TAB, BurgerIngredientLocators.BUNS_SECTION, "Булки"),
        (BurgerIngredientLocators.SAUCES_TAB, BurgerIngredientLocators.SAUCES_SECTION, "Соусы"),
        (BurgerIngredientLocators.TOPPINGS_TAB, BurgerIngredientLocators.TOPPINGS_SECTION, "Начинки")
    ])
    
    def test_click_tabs_scrolls_to_sections(self, driver, tab_locator, section_locator, expected_text):
       
        element = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(tab_locator)
        )

        ActionChains(driver).move_to_element(element).click().perform()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(section_locator)
        )

        assert driver.find_element(*BurgerIngredientLocators.ACTIVE_TAB).text == expected_text
   
                         
    