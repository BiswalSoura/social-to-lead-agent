import streamlit as st

from agent import ask_ai
from intent import is_high_intent
from tools import valid_email, capture_lead

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AutoStream AI Growth Advisor",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# PREMIUM STYLE
# -------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 900px;
}

.big-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 0px;
}

.subtle {
    color: #9ca3af;
    margin-bottom: 18px;
    font-size: 16px;
}

.stChatMessage {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    '<div class="big-title">🎬 AutoStream AI Growth Advisor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtle">Helping creators grow with AI-powered video editing</div>',
    unsafe_allow_html=True
)

with st.expander("💡 Suggested prompts"):
    st.markdown("""
- I make reels daily. Which plan suits me?  
- Tell me your pricing  
- Is Pro worth it for YouTube?  
- Too expensive for me  
- I want to join  
- I’m a beginner creator
""")

# -------------------------
# SESSION STATE
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
# SHOW CHAT
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# CHAT INPUT
# -------------------------
user_input = st.chat_input(
    "Ask about pricing, creator growth, plans, or getting started..."
)

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    reply = ""

    # -------------------------
    # LEAD CAPTURE MODE
    # -------------------------
    if st.session_state.lead_mode:

        lead = st.session_state.lead_data

        if not lead["name"]:
            lead["name"] = user_input.strip()
            reply = "Great to meet you! What's your best email address?"

        elif not lead["email"]:

            if not valid_email(user_input):
                reply = "That email doesn't look valid. Please enter a valid email address."
            else:
                lead["email"] = user_input.strip()
                reply = "Perfect. Which platform do you mainly create on? (YouTube / Instagram / TikTok)"

        elif not lead["platform"]:
            lead["platform"] = user_input.strip()

            reply = capture_lead(lead)

            st.session_state.lead_mode = False
            st.session_state.lead_data = {
                "name": None,
                "email": None,
                "platform": None
            }

    # -------------------------
    # NORMAL CHAT MODE
    # -------------------------
    else:

        if is_high_intent(user_input):

            reply = """
That's exciting — I'd love to help you get started.

What's your full name?
"""

            st.session_state.lead_mode = True

        else:

            history = "\n".join(
                [
                    f"{m['role']}: {m['content']}"
                    for m in st.session_state.messages[-10:]
                ]
            )

            try:
                reply = ask_ai(user_input, history)

            except Exception:
                reply = "I'm here to help with AutoStream pricing, plans, and creator growth."

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)