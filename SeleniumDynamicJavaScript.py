from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Replace with your path
driver.get("https://www.tiktok.com/login/phone-or-email/email")

try:
    # Wait for the email field to load
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"], input[name="email"]'))
    )
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')

    # Print details
    print("Email/Username Field:")
    print(f"  Type: {email_field.get_attribute('type')}")
    print(f"  Name: {email_field.get_attribute('name')}")
    print(f"  ID: {email_field.get_attribute('id')}")
    print(f"  Class: {email_field.get_attribute('class')}")

    print("\nPassword Field:")
    print(f"  Type: {password_field.get_attribute('type')}")
    print(f"  Name: {password_field.get_attribute('name')}")
    print(f"  ID: {password_field.get_attribute('id')}")
    print(f"  Class: {password_field.get_attribute('class')}")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
