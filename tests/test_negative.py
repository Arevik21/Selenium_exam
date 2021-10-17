from pages.base_page import Base
from functions.functions import ContactUS
import pytest

@pytest.mark.usefixtures('set_up')
class Test_negative(Base):
    
    @pytest.mark.parametrize('text1, text2, message', 
                            [
                                ('999#@', 'Field error- name field must contain only letters', \
                                'Name field accepts numbers and/or symbols, thought it should not.'),
                                ('', '* This field is required','Notification popup is missing or the message is wrong'),
                            ]
                            )
    def test_3(self, text1, text2, message):  #name field check
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name(text1)
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone("000000000")
        contact.input_country("Armenia")
        contact.input_company("BDG")
        contact.input_message("Hello")
        contact.submitclick()
        assert contact.popup().text == text2, message

    @pytest.mark.parametrize('text1, text2, message', 
                            [
                                ('wrongmailsample', '* Invalid email address','with invalid mail'),
                                ('', '* This field is required\n* Invalid email address','without email adress'),
                            ]
                            )
    def test_4(self, text1, text2, message):  #email field check
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email(text1)
        contact.input_telephone("000000000")
        contact.input_country("Armenia")
        contact.input_company("BDG")
        contact.input_message("Hello")
        contact.submitclick()
        assert contact.popup().text == text2, \
            f"The user should not be able login {message}. Notification popup is missing or its text is wrong"
    
    @pytest.mark.parametrize('text1, text2, message', 
                            [
                                ('wrongnumberformat', '* Invalid phone number', 'contain letters'),
                                ('#$%', '* Invalid phone number','contain symbols'),
                                ('', '* This field is required\n* Invalid phone number', 'be empty')
                            ]
                            )
    def test_5(self, text1, text2, message):  #telephone field check
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone(text1)
        contact.input_country("Armenia")
        contact.input_company("BDG")
        contact.input_message("Hello")
        contact.submitclick()
        assert contact.popup().text == text2, \
            f"Phone field should not {message}. Notification popup is missing or its text is wrong"
    
    @pytest.mark.parametrize('text1, text2, message',
                            [
                                ('#$%', 'Field Error- country field should contain only letters and spaces', 'symbols'),
                                (123, 'Field Error- country field should contain only letters and spaces','numbers')
                            ]
                            )
    def test_6(self, text1, text2, message):     #country field check
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone("000000000")
        contact.input_country(text1)
        contact.input_company("BDG")
        contact.input_message("Hello")
        contact.submitclick()
        assert contact.popup().text == text2, \
            f"Country field should not accept {message}. Notification popup is missing or its text is wrong."

    def test_7(self):     #message field check
        driver = self.driver
        contact = ContactUS(driver)
        contact.input_name("Arev")
        contact.input_email("arevsafar@gmail.com")
        contact.input_telephone("000000000")
        contact.input_country("Armenia")
        contact.input_company("BDG")
        contact.input_message("a"*181)
        contact.submitclick()
        assert contact.popup().text == 'Field Error- message field cannot have more than 180 letters', \
            'Message field contains more than 180 letters.Notification popup is missing or its text is wrong.'