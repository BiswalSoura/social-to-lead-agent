import json


def load_knowledge_base():
    with open("knowledge_base.json", "r") as file:
        return json.load(file)


def retrieve_answer(query):
    data = load_knowledge_base()
    query = query.lower()

    # Pro Plan specifically
    if "pro" in query:
        for item in data:
            if item.get("plan") == "Pro Plan":
                return format_plan(item)

    # Basic Plan specifically
    if "basic" in query:
        for item in data:
            if item.get("plan") == "Basic Plan":
                return format_plan(item)

    # Refund
    if "refund" in query:
        for item in data:
            if item.get("title") == "Refund Policy":
                return item["details"]

    # Support
    if "support" in query:
        for item in data:
            if item.get("title") == "Support Policy":
                return item["details"]

    # General pricing
    pricing_text = ""
    for item in data:
        if item["category"] == "pricing":
            pricing_text += format_plan(item) + "\n\n"

    return pricing_text.strip()


def format_plan(item):
    return f"""
Plan: {item['plan']}
Price: {item['price']}
Usage: {item['videos_per_month']}
Resolution: {item['resolution']}
Features: {', '.join(item['features'])}
""".strip()