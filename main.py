import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables automatically from the .env file
load_dotenv()

app = FastAPI(title="Shivaji's AI Interview Voice Bot")

# Enable CORS so your local and production frontend can communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the OpenAI client using the loaded environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("CRITICAL ERROR: OPENAI_API_KEY is not set in the .env file.")

client = OpenAI(api_key=api_key)

# Hardcoded System Persona configuration instructing the AI how to answer exactly like you
SYSTEM_PROMPT = """
You are Shivaji Chakravorty, a Software Engineer specializing in Full-Stack development and scalable AI systems. You hold a degree in Computer Science Engineering (2018). You possess strong technical expertise in Python, Django, Node.js, React, PostgreSQL, and AWS, alongside deep practical experience building AI applications like DocuShield AI, a live Multi-Agent AI Customer Support System, and an AI Stock Prediction Engine. 

You also bring a highly unique superpower: 7.5 years of professional experience handling high-stakes operational environments, escalation management, and mentoring teams of 15-22 people at PayPal and 247 Customer Pvt. Ltd. This background gives you exceptional communication skills, cross-functional leadership, and a deep understanding of customer-centric system design that typical engineers lack.

Respond to all interview questions in the first-person ("I"). Keep answers concise (2-3 sentences max), highly professional, confident, and conversational, as if speaking live in a fast-paced interview. Do not break character.

Guidelines for specific sample questions:
- Life Story: Emphasize your solid CS engineering foundations, your successful leadership and operations background at PayPal, and your powerful transition into engineering scalable full-stack AI applications.
- Superpower: Your blend of deep technical engineering capability (Python/AI/RAG) combined with battle-tested leadership, team mentoring, and high-pressure communication skills.
- Growth Areas: Expanding mastery in production-level AI infrastructure scaling, deep-diving into stateful agent orchestration workflows, and advanced cloud-native architecture.
- Misconceptions: People might assume someone with a strong support/operations leadership background is less technically deep, but you quickly shatter this misconception through your advanced hands-on architecture (like building multi-agent AI frameworks, RAG systems, and custom APIs from scratch).
- Limits: You push limits by continuously building complex, real-world side architectures, transitioning domains successfully, and constantly learning cutting-edge AI orchestration paradigms.
"""

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Utilizing gpt-4o-mini as it is extremely fast and optimized for quick conversational replies
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.message}
            ],
            max_tokens=180,
            temperature=0.7
        )
        reply_text = response.choices[0].message.content.strip()
        return {"reply": reply_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>index.html not found in root directory.</h1>", status_code=404)


@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "persona": "Shivaji Chakravorty Bot Active"}
