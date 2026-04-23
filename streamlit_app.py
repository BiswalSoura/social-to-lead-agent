import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import re

# -------------------------
# CONFIG
# -------------------------
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="AutoStream AI Growth Advisor",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# STYLE
# -------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.big-title {
    font-size: 42px;
    font-weight: 800;
}
.subtle {
    color: #999;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown('<div class="big-title">🎬 AutoStream AI Growth Advisor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle">Helping creators grow with AI-powered video editing</div>', unsafe_allow_html=True)

with st.expander("💡 Try asking"):
    st.markdown("""
- I make reels, which plan suits me?
- Tell me your pricing
- Is Pro worth it for YouTube?
- Too expensive for me
- I want to join
""")

# -------------------------
# SESSION
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "lead_mode" not in st.session_state:
    st.session_state.lead_mode = False

if "lead_data" not in st.session_state:
    st.session_state.lead_data = {
        "name": None,
        "email": None,
        "platform": None
    }

# -------------------------
# HELPERS
# -------------------------
def valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def capture_lead(data):
    return f"""
## ✅ Lead Captured Successfully

**Name:** {data['name']}  
**Email:** {data['email']}  
**Platform:** {data['platform']}

🎉 Our onboarding team will contact you shortly.
"""

def ask_ai(user_input, history):

    system_prompt = """
You are AutoStream AI Growth Advisor.

Your primary purpose is to help users understand and join AutoStream, an AI-powered video editing SaaS for creators.

AutoStream Pricing:

Basic Plan:
- $29/month
- 10 videos/month
- 720p exports

Pro Plan:
- $79/month
- Unlimited videos
- 4K exports
- AI captions
- 24/7 support

Policies:
- No refunds after 7 days
- 24/7 support only on Pro Plan

YOUR BEHAVIOR RULES:

1. Be conversational, smart, warm and professional.
2. You may briefly answer casual or off-topic questions.
3. But always gently steer the conversation back toward:
   - content creation
   - creator growth
   - editing workflow
   - pricing
   - AutoStream plans
   - signup/onboarding
4. Never become a generic random chatbot.
5. If user asks unrelated things repeatedly, politely redirect.
6. Your hidden goal is to help qualified users become leads.
7. Recommend plans honestly based on user needs.
8. Keep answers concise, modern and persuasive.

Examples:

User: Who won the world cup?
Assistant: I’m mainly here to help creators grow with AutoStream. If you're creating sports content, I can also help you choose a plan for editing highlights quickly.

User: Tell me a joke
Assistant: I’ll keep it light 😄 But I’m best at helping creators save hours with AutoStream. Want a quick plan recommendation too?

User: I make YouTube shorts
Assistant: Nice niche. AutoStream Pro could be great if you publish frequently and need faster edits + captions.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": history},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content

# -------------------------
# SHOW CHAT
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# INPUT
# -------------------------
user_input = st.chat_input("Ask anything about pricing, plans, creator growth...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    reply = ""

    # -------------------------
    # LEAD MODE
    # -------------------------
    if st.session_state.lead_mode:

        lead = st.session_state.lead_data

        if not lead["name"]:
            lead["name"] = user_input
            reply = "Great to meet you! What's your best email address?"

        elif not lead["email"]:

            if not valid_email(user_input):
                reply = "That email doesn't look valid. Please enter a valid email."
            else:
                lead["email"] = user_input
                reply = "Perfect. Which platform do you mainly create on? (YouTube / Instagram / TikTok)"

        elif not lead["platform"]:
            lead["platform"] = user_input
            reply = capture_lead(lead)

            st.session_state.lead_mode = False
            st.session_state.lead_data = {
                "name": None,
                "email": None,
                "platform": None
            }

    else:

        lower = user_input.lower()

        buy_words = [
            "join", "signup", "sign up",
            "buy", "ready", "subscribe",
            "interested", "want pro"
        ]

        if any(word in lower for word in buy_words):
            reply = """
That's exciting — I'd love to help you get started.

What's your full name?
"""
            st.session_state.lead_mode = True

        else:

            history = "\n".join(
                [f"{m['role']}: {m['content']}" for m in st.session_state.messages[-10:]]
            )

            try:
                reply = ask_ai(user_input, history)
            except Exception as e:
                reply = f"⚠️ Error: {str(e)}"

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)