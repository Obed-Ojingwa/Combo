from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (use the correct path to your chromedriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the webpage
driver.get("https://www.tiktok.com/login/phone-or-email")

# Wait for input fields to appear
try:
    # Wait for up to 10 seconds for the element(s) to load
    input_fields = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
    )
    # Print details of input fields
    for input_field in input_fields:
        print("Input Field:")
        print(f"  Type: {input_field.get_attribute('type')}")
        print(f"  Name: {input_field.get_attribute('name')}")
        print(f"  ID: {input_field.get_attribute('id')}")
        print(f"  Class: {input_field.get_attribute('class')}")
        print("-" * 20)
except Exception as e:
    print("Failed to locate input fields:", e)
finally:
    # Close the browser
    driver.quit()
