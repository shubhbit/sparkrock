import pytest
from app.login_locators import Login_Locators
from common.util import wait_for_element

class Login(object):
    def __init__(self, driver):
        self.web_url = pytest.config['web_url']
        self.driver = driver
        self.navigate_to_login()
        self.timer=10
        pytest.is_user_logged = False


    def navigate_to_login(self):
        self.driver.get(self.web_url)

    def enter_user_name(self, user):
        self.navigate_to_login()
        if wait_for_element(self.driver, self.timer, Login_Locators.USER_TEXT):
            element =  self.driver.find_element(*Login_Locators.USER_TEXT)
            element.send_keys(user)
        else:
            raise Exception("element {} not found".format(Login_Locators.USER_TEXT))

    def enter_user_password(self, password):
        if wait_for_element(self.driver, self.timer, Login_Locators.USER_PASSWORD):
            element =  self.driver.find_element(*Login_Locators.USER_PASSWORD)
            element.send_keys(password)
        else:
            raise Exception("element {} not found".format(Login_Locators.USER_PASSWORD))
    
    def click_login(self):
        if wait_for_element(self.driver, self.timer, Login_Locators.LOGIN_BUTTON):
            element =  self.driver.find_element(*Login_Locators.LOGIN_BUTTON)
            element.click()
            self.is_user_logged = True
        else:
            raise Exception("element {} not found".format(Login_Locators.LOGIN_BUTTON))

    def verify_login_success(self):
        return self.driver.current_url

    def login(self):
        self.navigate_to_login()
        self.enter_user_name(pytest.config['user_name'])
        self.enter_user_password(pytest.config['password'])
        self.click_login()