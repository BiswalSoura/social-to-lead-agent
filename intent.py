def detect_intent(user_message):
    message = user_message.lower()

    greeting_keywords = [
        "hi", "hello", "hey", "good morning", "good evening"
    ]

    inquiry_keywords = [
        "price", "pricing", "plan", "feature", "refund",
        "support", "cost", "subscription"
    ]

    lead_keywords = [
        "buy", "signup", "sign up", "purchase", "interested",
        "want pro", "want to try", "get started",
        "subscribe", "join", "ready"
    ]

    if any(word in message for word in greeting_keywords):
        return "greeting"

    elif any(word in message for word in lead_keywords):
        return "high_intent"

    elif any(word in message for word in inquiry_keywords):
        return "inquiry"

    return "general"