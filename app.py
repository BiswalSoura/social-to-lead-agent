from intent import detect_intent
from rag import retrieve_answer
from tools import mock_lead_capture, is_valid_email
from agent import ask_gemini

lead_state = {
    "collecting": False,
    "name": None,
    "email": None,
    "platform": None
}

valid_platforms = ["youtube", "instagram", "tiktok", "linkedin", "facebook"]

print("🎬 AutoStream AI Agent Ready")
print("Helping creators scale with smart video automation.")
print("Type 'exit' anytime to quit.\n")


while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Agent: Thanks for visiting AutoStream. Have a great day!")
        break

    # ----------------------------
    # LEAD COLLECTION FLOW
    # ----------------------------
    if lead_state["collecting"]:

        # Collect Name
        if not lead_state["name"]:
            lead_state["name"] = user_input
            print("Agent: Great to meet you! Please share your email address.")
            continue

        # Collect Email
        elif not lead_state["email"]:

            if not is_valid_email(user_input):
                print("Agent: That email looks invalid. Please enter a valid email address.")
                continue

            lead_state["email"] = user_input
            print("Agent: Perfect. Which platform do you primarily create content on?")
            print("Agent: (YouTube / Instagram / TikTok / LinkedIn / Facebook)")
            continue

        # Collect Platform
        elif not lead_state["platform"]:

            platform = user_input.lower()

            if platform not in valid_platforms:
                print("Agent: Please choose one of these platforms:")
                print("Agent: YouTube / Instagram / TikTok / LinkedIn / Facebook")
                continue

            lead_state["platform"] = user_input.title()

            mock_lead_capture(
                lead_state["name"],
                lead_state["email"],
                lead_state["platform"]
            )

            print("Agent: You're all set! Our onboarding team will contact you shortly.\n")

            # Reset memory
            lead_state = {
                "collecting": False,
                "name": None,
                "email": None,
                "platform": None
            }

            continue

    # ----------------------------
    # NORMAL FLOW
    # ----------------------------
    intent = detect_intent(user_input)

    # Greeting
    if intent == "greeting":
        print("Agent:", ask_gemini("Greet the user warmly as AutoStream assistant."))

    # Inquiry
    elif intent == "inquiry":
        print("Agent:", retrieve_answer(user_input))

    # High Intent
    elif intent == "high_intent":
        print("Agent: That's exciting! I'd love to help you get started.")
        print("Agent: Please share your full name.")
        lead_state["collecting"] = True

    # General AI Chat
    else:
        try:
            print("Agent:", ask_gemini(user_input))
        except:
            print("Agent: I'm here to help with AutoStream plans, creators, and video automation.")