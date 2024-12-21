from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch a browser (Chromium, Firefox, or WebKit)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Open the TikTok page
    page.goto("https://www.tiktok.com/login/phone-or-email/email")

    # Wait for the input fields to load
    email_field = page.query_selector('input[type="text"]')
    password_field = page.query_selector('input[type="password"]')

    # Print details of the fields
    print("Email/Username Field:")
    print(f"  Name: {email_field.get_attribute('name')}")
    print(f"  ID: {email_field.get_attribute('id')}")
    print(f"  Class: {email_field.get_attribute('class')}")

    print("\nPassword Field:")
    print(f"  Name: {password_field.get_attribute('name')}")
    print(f"  ID: {password_field.get_attribute('id')}")
    print(f"  Class: {password_field.get_attribute('class')}")

    # Close the browser
    browser.close()
