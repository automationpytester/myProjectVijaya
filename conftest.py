import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield  driver
    driver.quit()

@pytest.fixture(params=[{"Username": "Admin", "Password": "admin123"}])
def login_data(request):
    return request.param
@pytest.fixture(params=[{"Search": "Admin" "PIM" "Leave" "Time" "Recruitment"}])
def search_data(request):
    return request.param

''''@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    driver.get(url)
    request.cls.driver =driver
    yield
    driver.quit()'''

'''@pytest.fixture(params=[{"Search": "Charles " "David" "Dummy" "George AI"}])
def option_list(request):
    return request.param'''