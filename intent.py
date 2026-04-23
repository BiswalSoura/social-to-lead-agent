def is_high_intent(user_input):
    text = user_input.lower().strip()

    buy_words = [
        "join",
        "signup",
        "sign up",
        "buy",
        "ready",
        "subscribe",
        "interested",
        "want pro",
        "want basic",
        "trial",
        "demo",
        "book",
        "call",
        "start",
        "get started",
        "pricing please",
        "how do i join",
        "i want this",
        "register",
        "let's begin",
        "lets begin",
        "i'm ready",
        "im ready",
        "want to start",
        "need this",
        "use this",
        "purchase",
        "upgrade"
    ]

    return any(word in text for word in buy_words)