from selenium.webdriver.common.by import By

class Purchase_Locators(object):
    ITEM = (By.XPATH, "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item']//button[contains(text(), 'Add to cart')]")
    BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    CHECKOUT = (By.XPATH, "//button[@id='checkout']")
    FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE = (By.XPATH, "//input[@id='continue']")
    FINISH = (By.XPATH, "//button[@id='finish']")
    SUCCESS = (By.XPATH, "//h2[text()='Thank you for your order!']")
    BACK_HOME = (By.XPATH, "//button[@id='back-to-products']")