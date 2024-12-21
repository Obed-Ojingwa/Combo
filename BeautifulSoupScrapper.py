import requests
from bs4 import BeautifulSoup

url = "https://www.tiktok.com/login/phone-or-email/email"

# Custom headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers)

# Check if successful
if response.status_code == 200:
    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the input fields
    email_field = soup.find('input', {'type': 'text'}) or soup.find('input', {'name': 'email'})
    password_field = soup.find('input', {'type': 'password'})
    
    # Print the attributes of the fields
    print("Email/Username Field:")
    if email_field:
        print(f"  Name: {email_field.get('name')}")
        print(f"  ID: {email_field.get('id')}")
        print(f"  Class: {email_field.get('class')}")
    else:
        print("  Not found in static HTML.")

    print("\nPassword Field:")
    if password_field:
        print(f"  Name: {password_field.get('name')}")
        print(f"  ID: {password_field.get('id')}")
        print(f"  Class: {password_field.get('class')}")
    else:
        print("  Not found in static HTML.")
else:
    print(f"Failed to fetch the page. Status Code: {response.status_code}")
