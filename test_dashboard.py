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


def test_dashboard(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    print(driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"))
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("scrolldown successfully")

def test_search(setup):
    driver = setup
    search_data =driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']")
    for find in search_data:
        if find.text == "Admin":
            find.click()
        print(find)
time.sleep(10)


