import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def ask_gemini(user_message):
    prompt = f"""
You are AutoStream AI assistant.

AutoStream is a SaaS platform for automated video editing tools for content creators.

Plans:
Basic Plan = $29/month, 10 videos/month, 720p
Pro Plan = $79/month, Unlimited videos, 4K, AI captions, 24/7 support

Policies:
No refunds after 7 days.
24/7 support only on Pro Plan.

Be helpful, short, professional and conversational.

User: {user_message}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return "Hello! I'm here to help with AutoStream plans, pricing, and creator growth."