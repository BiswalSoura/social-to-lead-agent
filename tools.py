import re


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def mock_lead_capture(name, email, platform):
    print("\n✅ Lead captured successfully!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")