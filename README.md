# Rehnuma (رہنما) — AI Assistant for Pakistani Government Services

Rehnuma ("The Guide") is an AI-powered assistant that helps Pakistani citizens navigate government services — CNIC and passport processes (NADRA), tax filing (FBR), and utility bills — in simple, step-by-step language.

Many citizens struggle to find clear, reliable guidance for government procedures. Rehnuma makes that guidance accessible through a conversational AI, while always directing users to verify critical details with official sources.

## Why this project

Government processes in Pakistan are often confusing and scattered across multiple departments. Rehnuma brings clear guidance into one place, designed with a strong focus on **responsible AI** — it never invents fees or deadlines, and always points users to official verification.

## Features

- Clear, step-by-step guidance for common government services
- Grounded, honest responses — never fabricates fees, dates, or addresses
- Always reminds users to verify important details with official sources
- Stays focused on its domain (politely redirects off-topic questions)

## Tech Stack

- **Python**
- **Groq API** (Llama 3.3 70B) for language understanding
- **python-dotenv** for secure API key handling
- System-prompt engineering for controlled, reliable behavior

## How to Run

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/aakash-halepoto/rehnuma-gov-assistant.git
   cd rehnuma-gov-assistant
   \`\`\`

2. Set up a virtual environment and install dependencies:
   \`\`\`bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   \`\`\`

3. Add your Groq API key to a \`.env\` file:
   \`\`\`
   GROQ_API_KEY=your_key_here
   \`\`\`

4. Run:
   \`\`\`bash
   python assistant.py
   \`\`\`

## Project Status

 **In active development.** This project grows as I learn — built as part of my journey into AI engineering.

**Roadmap:**
- [x] Core assistant with system-prompt-controlled behavior
- [ ] Knowledge base grounding (retrieval-augmented responses)
- [ ] Conversation memory
- [ ] Interactive CLI
- [ ] Web interface

## Disclaimer

Rehnuma provides general guidance only. Always verify official procedures, fees, and requirements with the relevant government department or official website.