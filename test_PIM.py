import time
import traceback

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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

def test_PIM(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]"))
    ).send_keys("Charles")

    option_list=driver.find_elements(By.CLASS_NAME,"oxd-autocomplete-dropdown")
    for suggest in option_list:
        if suggest.text== "Charles":
            suggest.click()
            assert suggest == "Charles","Selected successfully"
            print("Charles selected successfully")
            time.sleep(10)
