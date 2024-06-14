import pytest
from app.purchase_locators import Purchase_Locators
from common.util import wait_for_element

class Purchase(object):

    def __init__(self, driver):
        self.driver = driver
        self.inventory_url = "http://www.saucedemo.com/inventory.php"
        self.timer = 10
        if not pytest.is_user_logged:
            pytest.login_instance.login()

    def navigate_to_inventory(self):
        self.driver.get(self.inventory_url)

    def add_item_to_cart(self):
        if not pytest.is_user_logged:
            pytest.login_instance.login()
        if wait_for_element(self.driver, self.timer, Purchase_Locators.ITEM):
            element = self.driver.find_element(*Purchase_Locators.ITEM)
            element.click()
        else:
            raise Exception("element not found")

    def checkout(self):
        if wait_for_element(self.driver, self.timer, Purchase_Locators.BADGE):
            element = self.driver.find_element(*Purchase_Locators.BADGE)
            element.click()
            element = self.driver.find_element(*Purchase_Locators.CHECKOUT)
            element.click()
        else:
            raise Exception("element not found")

    
    def fill_details(self, first_name, last_name, postal_code):
        if wait_for_element(self.driver, self.timer, Purchase_Locators.FIRST_NAME):
            element = self.driver.find_element(*Purchase_Locators.FIRST_NAME)
            element.send_keys(first_name)
            element = self.driver.find_element(*Purchase_Locators.LAST_NAME)
            element.send_keys(last_name)
            element = self.driver.find_element(*Purchase_Locators.POSTAL_CODE)
            element.send_keys(postal_code)
            element = self.driver.find_element(*Purchase_Locators.CONTINUE)
            element.click()
        else:
            raise Exception("element not found")

    def finish(self):
        if wait_for_element(self.driver, self.timer, Purchase_Locators.FINISH):
            element = self.driver.find_element(*Purchase_Locators.FINISH)
            element.click()
        else:
            raise Exception("element not found")

    def verify_success(self):
        if wait_for_element(self.driver, self.timer, Purchase_Locators.SUCCESS):
            element = self.driver.find_element(*Purchase_Locators.SUCCESS)
            return element.text
        else:
            raise Exception("element not found")

    def back_home(self):
        if wait_for_element(self.driver, self.timer, Purchase_Locators.BACK_HOME):
            element = self.driver.find_element(*Purchase_Locators.BACK_HOME)
            element.click()
        else:
            raise Exception("element not found")

