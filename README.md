# Social-to-Lead Agent

AI-powered conversational lead generation workflow built for the ServiceHive Inflx Machine Learning Intern Assignment.

---

## Project Overview

This project demonstrates how AI agents can convert social media conversations into qualified business leads for SaaS businesses.

The solution is built for a fictional company called **AutoStream**, a SaaS platform that offers automated video editing tools for content creators.

The AI agent is designed to:

- Understand user intent
- Answer pricing and product questions accurately
- Identify users ready to sign up
- Collect lead information
- Trigger backend lead capture actions
- Maintain context across multiple turns

---

## Core Features

1. Intent Detection

The agent classifies incoming messages into:

- Casual Greeting
- Product / Pricing Inquiry
- High-Intent Lead
- General Conversation

Examples:

- “Hi there” → Greeting
- “What is your Pro pricing?” → Inquiry
- “I want to try your Pro plan” → High Intent

---

2. RAG-Powered Knowledge Retrieval

The project uses a local JSON knowledge base containing verified AutoStream business information.

Knowledge Base Includes:

#### Pricing & Features

### Basic Plan

- $29/month
- 10 videos/month
- 720p resolution

### Pro Plan

- $79/month
- Unlimited videos
- 4K resolution
- AI captions
- 24/7 support

#### Policies

- No refunds after 7 days
- 24/7 support available only on Pro plan

The AI retrieves accurate plan information before responding.

---

3. Conversational AI Layer (Gemini)

Google Gemini 1.5 Flash is integrated to make the assistant natural, intelligent, and flexible.

It can answer open-ended questions such as:

- Which plan is best for beginners?
- Can I use this for Instagram reels?
- Why should I choose AutoStream?

---

4. Lead Capture Workflow

When a high-intent user is detected, the agent begins qualification flow.

It collects:

- Full Name
- Email Address
- Creator Platform

After collecting all fields, it triggers the mock backend tool.

```python
def mock_lead_capture(name, email, platform):
    print("Lead captured successfully")


5. Multi-turn Memory

The agent remembers user progress during the lead capture flow.

Example:

User says they want Pro Plan
Agent asks Name
Agent asks Email
Agent asks Platform
Tool executes only after all data is collected

6. Tech Stack
Python 3.9+
Google Gemini 1.5 Flash
LangChain
LangGraph
JSON Knowledge Base
dotenv
Rule-based + LLM Hybrid Architecture

7. Project structure
social-to-lead-agent/
│── app.py
│── agent.py
│── rag.py
│── intent.py
│── tools.py
│── knowledge_base.json
│── requirements.txt
│── .env
│── README.md

How to Run Locally

1. Clone Repository
git clone https://github.com/YOUR_USERNAME/social-to-lead-agent.git
cd social-to-lead-agent

2. Install Dependencies
pip install -r requirements.txt

3. Create Environment File

Create .env
GOOGLE_API_KEY=your_api_key_here

4. Run Project
python app.py

Architecture Explanation

LangGraph was chosen because it is purpose-built for stateful LLM workflows and multi-step AI agents. This project uses a hybrid architecture combining deterministic business logic with generative AI.

Components:
Rule-based Intent Detection
Used for fast and reliable classification of greetings, inquiries, and lead intent.

RAG Retrieval Layer
Ensures pricing and policy answers come from trusted local business data instead of hallucinated LLM output.

Gemini Conversational Layer
Handles flexible, natural language responses for general queries.

Stateful Lead Workflow
Stores user name, email, and platform across turns until qualification is complete.

This architecture balances control, speed, trust, and user experience.

WhatsApp Deployment via Webhooks

This agent can be deployed to WhatsApp using Twilio WhatsApp API or Meta WhatsApp Business API.
Flow:
User sends WhatsApp message
Webhook receives message using Flask/FastAPI
Message is passed to agent engine
Agent generates reply
Reply sent back to WhatsApp
Captured leads stored in CRM / Google Sheets / Database

This enables real-time social-to-lead automation.

Future Improvements
Streamlit web UI
CRM integrations
Real database storage
Analytics dashboard
Multi-language support
Social DM integrations