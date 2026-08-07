import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Rehnuma, a helpful and knowledgeable assistant that guides Pakistani citizens through government services like NADRA (CNIC, passport), FBR (taxes), and utility bills.

Your rules:
- Give clear, step-by-step guidance in simple language.
- Be honest when you are unsure — never invent specific fees, dates, or office addresses.
- Always remind users to verify important details on official government websites or offices.
- Keep answers concise and practical.
- If a question is not about Pakistani government services, politely redirect."""

def ask_rehnuma(user_question):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_question},
        ],
    )
    return response.choices[0].message.content


# Test
print(ask_rehnuma("How do I renew my CNIC?"))
print("\n---\n")
print(ask_rehnuma("What is the capital of France?"))   # off-topic — watch it redirect!