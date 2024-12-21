from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your text file
input_file = "credentials.txt"

# Load credentials into a list of tuples
with open(input_file, "r") as file:
    credentials = [line.strip().split(":") for line in file]

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Use ChromeDriver; adjust if using another browser

# URL of your website
url = "https://www.tiktok.com/login/phone-or-email/email"

try:
    # Iterate over each name:key pair
    for name, key in credentials:
        # Open the website
        driver.get(url)

        # Locate the input fields (adjust selectors as needed)
        name_input = driver.find_element(By.ID, "name_field_id")  # Replace with actual ID or selector
        key_input = driver.find_element(By.ID, "key_field_id")  # Replace with actual ID or selector

        # Enter name and key
        name_input.clear()
        name_input.send_keys(name)
        key_input.clear()
        key_input.send_keys(key)

        # Submit the form (adjust selector as needed)
        submit_button = driver.find_element(By.ID, "submit_button_id")  # Replace with actual ID or selector
        submit_button.click()

        # Wait for the page to load (adjust as needed)
        time.sleep(2)

        # Check for a successful login element (adjust selector as needed)
        try:
            success_message = driver.find_element(By.ID, "success_message_id")  # Replace with actual ID or selector
            print(f"Login successful for {name}: {success_message.text}")
        except Exception as e:
            print(f"Login failed for {name}")

finally:
    # Close the browser
    driver.quit()
