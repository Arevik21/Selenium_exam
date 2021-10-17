from typing import Text
from locators.locators import LocatorsXPath
from time import sleep


class ContactUS():
    def __init__(self,driver):
        self.driver = driver
        self.name = LocatorsXPath.name
        self.email = LocatorsXPath.email
        self.telephone = LocatorsXPath.telephone
        self.country = LocatorsXPath.country
        self.company = LocatorsXPath.company
        self.message = LocatorsXPath.message
        self.submit = LocatorsXPath.submit
        self.clear = LocatorsXPath.clear
        self.pop = LocatorsXPath.feedbacksent
        self.field = LocatorsXPath.formfields

    def popup(self):
        popuptext = self.driver.find_element_by_xpath(self.pop)
        return(popuptext)

    def formfield(self):
        fields = self.driver.find_elements_by_xpath(self.field)
        return(fields)

    def input_name(self,text):
        inputname = self.driver.find_element_by_xpath(self.name)
        inputname.send_keys(text)
        sleep(1)

    def input_email(self,text):
        inputemail = self.driver.find_element_by_xpath(self.email)
        inputemail.send_keys(text)
        sleep(1)

    def input_telephone(self,text):
        inputtel = self.driver.find_element_by_xpath(self.telephone)
        inputtel.send_keys(text)
        sleep(1)

    def input_country(self,text):
        inputcountry = self.driver.find_element_by_xpath(self.country)
        inputcountry.send_keys(text)
        sleep(1)
    
    def input_company(self,text):
        inputcompany = self.driver.find_element_by_xpath(self.company)
        inputcompany.send_keys(text)
        sleep(1)

    def input_message(self,text):
        inputmessage = self.driver.find_element_by_xpath(self.message)
        inputmessage.send_keys(text)
        sleep(1)
        
    def submitclick(self):
        subm = self.driver.find_element_by_xpath(self.submit)
        subm.click()
        sleep(5)

    def clearclick(self):
        cl = self.driver.find_element_by_xpath(self.clear)
        cl.click()
        sleep(5)
