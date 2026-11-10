Shivaji's AI Interview Voice Bot

A universally user-friendly, responsive web application featuring an interactive interview voice bot designed to simulate live technical and behavioral assessments. The bot is hardcoded to respond exactly as Shivaji Chakravorty would, drawing directly from his technical background and leadership experience.

🌐 Live Interactive Demo

👉 Click Here: https://web-production-66d74.up.railway.app/ to Test the Live Application (Replace this with your real Railway public link)

✨ Features & Submission Compliance

• Zero Technical Setup for Testers: Built entirely on top of browser-native Web Audio APIs (webkitSpeechRecognition & speechSynthesis). Anyone can open the app on a browser and immediately begin testing without code installations.

• No API Key Exposure: System authentication is processed entirely on a secured, isolated backend layer. Reviewers are never prompted to provide an API key.

• Conversational Logic: Designed to dynamically parse core profile questions using a hardcoded persona prompt layer powered by gpt-4o-mini.


🎭 The Persona Architecture

The application forces the underlying LLM to adopt Shivaji's real professional identity in the first person ("I"):
• Foundations: Computer Science Engineering Graduate (2018) with a modern technical focus in Python, FastAPI, Django, Node.js, and RAG architectures.

• Proven Expertise: Highlighted engineering architectures including DocuShield AI, a live Multi-Agent AI Customer Support System, and an AI Stock Prediction Engine.

• The Leadership Superpower: Over 7.5 years of professional high-stakes operation engineering experience managing critical escalation matrices and leading operational pipelines for engineering teams of 15–22 specialists at PayPal and 247 Customer Pvt. Ltd.


🎙️ Sample Questions to Test

You can click the microphone button and ask the bot any variation of the following interview items:
1. "What should we know about your life story in a few sentences?"
2. "What’s your #1 superpower?"
3. "What are the top 3 areas you’d like to grow in?"
4. "What misconception do your coworkers have about you?"
5. "How do you push your boundaries and limits?"


🛠️ Tech Stack & Modular Structure

The project is architected with a decoupled frontend interface served securely under a single origin by a fast backend application layer to handle secure SSL data flow:

• Frontend (index.html): Self-contained, responsive layout with embedded CSS. Leverages browser native Web Speech APIs for speech-to-text transcription and text-to-speech outputs.

• Backend Framework (main.py): Structured utilizing FastAPI, enabling strict typed data verification through Pydantic and safe multi-origin resource sharing via CORS middleware.

• Core API Client: Asynchronous openai SDK configuration communicating securely with backend system configurations.

interview-voicebot/
├── index.html          # Frontend Voice Interface & Native Scripting
├── main.py            # FastAPI Server Application & Persona Logic
├── requirements.txt   # Core Project Dependencies
├── Procfile           # Production Engine Command Rules
└── .gitignore         # Secret variable safety file mappings



