import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()
    