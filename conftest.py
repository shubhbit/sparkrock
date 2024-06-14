import pytest
from selenium import webdriver
from app.login import Login
from app.purchase import Purchase

@pytest.fixture(scope='session', autouse=True)
def setup():
    pytest.driver = webdriver.Firefox()
    pytest.login_instance = Login(pytest.driver)
    pytest.purchase_instance = Purchase(pytest.driver)
    yield
    del pytest.login_instance
    del pytest.purchase_instance
    pytest.driver.quit()

@pytest.fixture(scope='session', autouse=True)
def read_config():
    pytest.config = {}
    with open('conf.env', 'r') as f:
        for line in f:
            line = line.split("=")
            pytest.config[line[0]] = line[1].replace("\n", "")
    yield
    del pytest.config