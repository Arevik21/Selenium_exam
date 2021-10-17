from time import sleep
from typing import Counter
from functions.functions import ContactUS
from pages.base_page import Base
import pytest

@pytest.mark.usefixtures('set_up')
class Test_positive(Base):
    def test_0(self):      #submitting without filling in not required fields
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone("000000000")
        contact.submitclick()
        assert contact.popup().text == "Feedback has been sent to the administrator", 'An error occurred, thought not filled in fields can be empty'

    def test_1(self):     #submit button
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone("000000000")
        contact.input_country("Armenia")
        contact.input_company("BDG")
        contact.input_message("Hello")
        contact.submitclick()
        assert contact.popup().text == "Feedback has been sent to the administrator", "Notification popup is missing or its text is wrong"

    def test_2(self):    #clear button
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone("000000000")
        contact.input_country("Armenia")
        contact.input_company("BDG")
        contact.input_message("Hello")
        contact.clearclick()
        values = [value.get_attribute('value') for value in contact.formfield()]
        for i in values:
            assert i == "", "Clear button doesn't work properly. Some fields are not empty."

