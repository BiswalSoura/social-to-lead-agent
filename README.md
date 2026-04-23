# Social-to-Lead Agent

AI-powered conversational lead generation workflow built for the **ServiceHive Inflx Machine Learning Intern Assignment**.

A production-style AI assistant that converts user conversations into qualified SaaS leads through intelligent chat, pricing guidance, and automated onboarding flow.

---

# Live Demo

https://social-to-lead-agent.streamlit.app/

---

# Project Overview

This project simulates how modern AI agents can convert inbound conversations into business leads for SaaS companies.

The solution is built for a fictional company called **AutoStream**, a SaaS platform that offers automated video editing tools for content creators.

The AI assistant is designed to:

- Understand user intent
- Answer pricing and product questions accurately
- Identify high-intent users
- Recommend suitable plans
- Collect lead information
- Trigger lead capture workflow
- Maintain context across multiple turns
- Redirect users back toward business goals

---

# Core Features

## 1. Intent Detection

The agent intelligently detects buying signals and user intent.

Supported categories:

- Casual Greeting
- Product / Pricing Inquiry
- High-Intent Lead
- General Conversation

Examples:

- “Hi there” → Greeting  
- “What is your Pro pricing?” → Inquiry  
- “I want to get started” → High Intent  
- “Which plan suits creators?” → Consultative Query

---

## 2. RAG-Powered Knowledge Retrieval

The project uses a **local JSON knowledge base** to provide accurate business information.

File used:

```text
knowledge_base.json

The assistant retrieves verified data before responding.

Pricing & Features
Basic Plan
$29/month
10 videos/month
720p exports
Pro Plan
$79/month
Unlimited videos
4K exports
AI captions
24/7 support

Policies
No refunds after 7 days
24/7 support available only on Pro Plan

3. Conversational AI Layer
Powered using Groq-hosted Llama 3.1 for fast and natural responses.
The assistant can answer flexible questions such as:

Which plan is best for beginners?
Can I use this for Instagram reels?
Why should I choose AutoStream?
Is Pro worth it for YouTube creators?

4. Lead Capture Workflow

When a high-intent user is detected, the agent automatically begins onboarding flow.

It collects:

Full Name
Email Address
Creator Platform

After collecting all required fields:
Lead captured successfully

5. Multi-Turn Memory

The chatbot remembers user progress during lead capture.

Example Flow

User: I want to join
Agent: What's your full name?
User: User
Agent: What's your email?
User: user@email.com

Agent: Which platform do you create on?
User: YouTube

Lead captured successfully.

Tech Stack
Python 3.9+
Streamlit
Groq API
Llama 3.1 8B Instant
JSON Knowledge Base
dotenv
Modular Python Architecture


How to Run Locally
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/social-to-lead-agent.git
cd social-to-lead-agent

2. Install Dependencies
pip install -r requirements.txt

3. Create Environment File
Create .env
GROQ_API_KEY=your_api_key_here

4. Run Application
streamlit run streamlit_app.py

Architecture Explanation

This project uses a modular production-style architecture combining deterministic business logic with modern LLM intelligence.

Components :

Streamlit UI Layer
Handles public web interface and multi-user chat sessions.

Intent Detection Layer
Detects signup readiness and buying signals quickly using lightweight logic.

RAG Retrieval Layer
Reads trusted company data from knowledge_base.json using rag.py.

LLM Conversational Layer
Groq-hosted Llama model powers natural, persuasive, and context-aware responses.

Stateful Lead Workflow
Stores name, email, and platform across turns until lead qualification completes.

This architecture balances:

Speed
Accuracy
Control
Scalability
User Experience

WhatsApp Deployment via Webhooks

This assistant can be deployed to WhatsApp using:

Twilio WhatsApp API
Meta WhatsApp Business API

Flow
User sends WhatsApp message
Webhook receives message (FastAPI / Flask)
Message routed to AI engine
Agent generates reply
Response sent back to WhatsApp
Qualified leads stored in CRM / Sheets / Database

This enables real-time social-to-lead automation.

Future Improvements:
CRM integrations
Database lead storage
Analytics dashboard
Multi-language support
Social DM integrations
Human handoff mode
Team inbox workflow
Conversion analytics


Author
Built by Soura Biswal as part of ML Engineer / AI Product portfolio development.