from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.tiktok.com/login/phone-or-email")

    # Wait for input fields to load
    input_fields = page.query_selector_all("input")

    # Print details of input fields
    for input_field in input_fields:
        print("Input Field:")
        print(f"  Type: {input_field.get_attribute('type')}")
        print(f"  Name: {input_field.get_attribute('name')}")
        print(f"  ID: {input_field.get_attribute('id')}")
        print(f"  Class: {input_field.get_attribute('class')}")
        print("-" * 20)

    browser.close()
