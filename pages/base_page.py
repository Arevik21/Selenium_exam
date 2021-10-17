from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import pytest

class Base:
    @pytest.fixture()
    def set_up(self):
        PATH = '/usr/local/bin/chromedriver'
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.seleniumframework.com/Practiceform/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit() 