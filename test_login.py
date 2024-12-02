import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome() # Make sure to have the ChromeDriver installed
    driver.implicitly_wait(10)  # Optional: waits for elements to be available
    yield driver
    driver.quit()


def test_login_valid (setup,login_data):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))
    username_input = driver.find_element(By.XPATH,"//input[@placeholder='Username']")
    username_input.send_keys(login_data['Username'])
    password_input = driver.find_element(By.NAME , "password")
    password_input.send_keys(login_data['Password'])
    time.sleep(5)
    Login_button =driver.find_element(By.XPATH,"//button[@type='submit']")
    Login_button.click()
    print("Login successfully")








