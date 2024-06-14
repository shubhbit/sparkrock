from selenium.webdriver.common.by import By

class Login_Locators(object):
    USER_TEXT = (By.XPATH, "//input[@id='user-name']")
    USER_PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")


