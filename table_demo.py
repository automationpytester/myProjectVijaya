from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_table_search():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
        driver.maximize_window()

        time.sleep(2)

        search_box = driver.find_element(By.XPATH, "//input[@type='search']")

        search_box.clear()
        search_box.send_keys("New York")
        time.sleep(2)

        result_rows = driver.find_elements(By.CSS_SELECTOR, "#results-table tbody tr")  
        visible_rows = [row for row in result_rows if row.is_displayed()]

        assert len(visible_rows) == 5, f"Expected 5 entries, but found {len(visible_rows)}"

        total_entries_text = driver.find_element(By.ID, "total-entries")  
        assert "24 total entries" in total_entries_text.text, "Total entries count does not match expected value"

        print("Test passed: Search results are correctly displayed!")

    except AssertionError as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_table_search()
