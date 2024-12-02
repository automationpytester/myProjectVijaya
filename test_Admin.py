import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
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

def test_Admin(setup):
    driver= setup
    name_input = driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
    name_input.send_keys("Admin")

