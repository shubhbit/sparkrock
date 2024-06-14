from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, timer, element):
    try:
        WebDriverWait(driver, timer).until(
            EC.presence_of_element_located(element)
        )
        return True
    except Exception as e:
        return False