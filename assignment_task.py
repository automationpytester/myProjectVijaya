#Assignment of Vijaya Ashok Bhaigade
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from jsonschema import validate


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


    BASE_URL = "http://mockhospitalmanagement.com"
    API_URL = "http://mockapi.com/patients"

    class TestPatientManagement(pytest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(10)
            cls.driver.get(BASE_URL)

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()

        def test_create_patient_record_valid(self):
            driver = self.driver
            driver.get("http://mockhospitalmanagement.com")
            driver.find_element(By.ID, "create-patient").click()
            driver.find_element(By.ID, "name").send_keys("Vijaya")
            driver.find_element(By.ID, "email").send_keys("vijaya.b@example.com")
            driver.find_element(By.ID, "submit").click()

            success_message = driver.find_element(By.CLASS_NAME, "success-message").text
            self.assertIn("Patient created successfully", success_message)

        def test_create_patient_record_invalid(self):
            driver = self.driver
            driver.find_element(By.ID, "create-patient").click()
            driver.find_element(By.ID, "email").send_keys("invalid-email")
            driver.find_element(By.ID, "submit").click()

            error_message = driver.find_element(By.CLASS_NAME, "error-message").text
            self.assertIn("Invalid email format", error_message)


        def test_search_patient_valid(self):
            driver = self.driver
            search_box = driver.find_element(By.ID, "search")
            search_box.send_keys("Vijaya")
            search_box.send_keys(Keys.RETURN)

            search_result = driver.find_element(By.CLASS_NAME, "patient-record").text
            self.assertIn("Vijaya", search_result)

        def test_search_patient_invalid(self):
            driver = self.driver
            search_box = driver.find_element(By.ID, "search")
            search_box.send_keys("Unknown Patient")
            search_box.send_keys(Keys.RETURN)

            no_result_message = driver.find_element(By.CLASS_NAME, "no-result-message").text
            self.assertIn("No records found", no_result_message)

        #__ API Testing
        def test_api_create_patient(self):
            payload = {
                "name": "Vijaya",
                "email": "vijaya.b@example.com",
                "age": 22
            }
            response = requests.post(f"{API_URL}", json=payload)
            self.assertEqual(response.status_code, 201)

        def test_api_schema_validation(self):
            response = requests.get(f"{API_URL}/1")
            schema = {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "age": {"type": "integer"}
                },
                "required": ["id", "name", "email", "age"]
            }
            validate(instance=response.json(), schema=schema)

    if __name__ == "__main__":
        pytest.main()
