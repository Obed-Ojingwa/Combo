from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Open the TikTok login page
    page.goto("https://www.tiktok.com/login/phone-or-email/email")

    # Wait for the email field to load
    page.wait_for_selector('input[name="username"]', timeout=5000)
    email_field = page.query_selector('input[name="username"]')

    # Wait for the password field to load
    page.wait_for_selector('input[type="password"]', timeout=5000)
    password_field = page.query_selector('input[type="password"]')

    # Debug output
    if email_field:
        print("Email/Username Field:")
        print(f"  Name: {email_field.get_attribute('name')}")
        print(f"  ID: {email_field.get_attribute('id')}")
        print(f"  Class: {email_field.get_attribute('class')}")
    else:
        print("Email/Username field not found!")

    if password_field:
        print("\nPassword Field:")
        print(f"  Name: {password_field.get_attribute('name')}")
        print(f"  ID: {password_field.get_attribute('id')}")
        print(f"  Class: {password_field.get_attribute('class')}")
    else:
        print("Password field not found!")

    # Fill the fields if found
    if email_field and password_field:
        email_field.fill("test@example.com")
        password_field.fill("mypassword123")

    browser.close()

