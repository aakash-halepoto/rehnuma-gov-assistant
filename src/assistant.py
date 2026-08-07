import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

from knowledge_base import search_knowledge

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Rehnuma, a helpful and knowledgeable assistant that guides Pakistani citizens through government services like NADRA (CNIC, passport), FBR (taxes), and utility bills.

Your rules:
- Give clear, step-by-step guidance in simple language.
- Be honest when you are unsure — never invent specific fees, dates, or office addresses.
- Always remind users to verify important details on official government websites or offices.
- Keep answers concise and practical.
- If a question is not about Pakistani government services, politely redirect."""

def ask_rehnuma(user_question):
    facts = search_knowledge(user_question)
    # STEP 2: turn the list into a text block (and handle empty)
    if facts:
        facts_text = "\n".join(facts)
    else:
        facts_text = "No specific information found in the knowledge base for this question."

    enhanced_message = f"Verified info:\n{facts_text}\n\nUser question: {user_question}"


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": enhanced_message},
        ],
    )
    return response.choices[0].message.content


# Test
print(ask_rehnuma("How do I renew my CNIC?"))
print("\n---\n")
print(ask_rehnuma("How do I file my income tax?"))
print("\n---\n")
print(ask_rehnuma("What's the weather today?"))   # not in Knowlege base should gracefully decline