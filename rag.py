import json
import os


def get_knowledge():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "knowledge_base.json")

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        sections = []

        for item in data:

            if item.get("category") == "pricing":
                section = f"""
{item.get('plan', 'Plan')}
- Price: {item.get('price', 'N/A')}
- Videos Per Month: {item.get('videos_per_month', 'N/A')}
- Resolution: {item.get('resolution', 'N/A')}
- Features: {', '.join(item.get('features', []))}
"""
                sections.append(section.strip())

            elif item.get("category") == "policy":
                section = f"""
{item.get('title', 'Policy')}
- {item.get('details', 'N/A')}
"""
                sections.append(section.strip())

        return "\n\n".join(sections)

    except Exception:
        return """
Basic Plan
- Price: $29/month
- Videos Per Month: 10 videos/month
- Resolution: 720p

Pro Plan
- Price: $79/month
- Videos Per Month: Unlimited videos
- Resolution: 4K
- Features: AI captions, 24/7 support
"""