import re


def valid_email(email):
    email = email.strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(pattern, email) is not None


def capture_lead(data):

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    platform = data.get("platform", "").strip()

    return f"""
## ✅ Lead Captured Successfully

**Name:** {name}  
**Email:** {email}  
**Platform:** {platform}

🎉 Our onboarding team will contact you shortly.
"""