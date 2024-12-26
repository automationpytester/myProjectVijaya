Overview
This script automates the validation of the search functionality on the Selenium Playground Table Search Demo. The script performs the following tasks:
Navigates to the demo page.
Searches for the term "New York."
Verifies that 5 rows are displayed in the search results.
Confirms that the page displays "24 total entries."

Prerequisites
To run this script, you need:
Python 3.8 or higher: Install it from Python.org.
Google Chrome Browser: Ensure it's installed and up-to-date.
ChromeDriver: Download the version matching your Chrome browser from ChromeDriver.
Selenium Library: Install it using:
bash Copy code
pip install selenium

Setup Instructions
Clone or download the script file (table_demo.py) into your project directory.
Ensure chromedriver is accessible in your system's PATH or update the script to specify the exact path to chromedriver.
Running the Script
Open a terminal and navigate to the script's directory.
Run the script using:
bash
Copy code
pytest table_demo.py
The browser will open, execute the test, and close automatically.

Notes
Error Handling: The script will output a message indicating success or failure of the test.
Adjustments: Modify the sleep times if necessary, based on the speed of your internet and system performance.
Troubleshooting
If the script fails to run:
Verify the correctness of the website URL.
Check the ChromeDriver version compatibility.
Ensure all dependencies are installed correctly.
