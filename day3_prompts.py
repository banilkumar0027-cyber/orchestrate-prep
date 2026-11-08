
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)

user_question = "My package is late. What should I do?"

system_messages = [
    "You are a friendly assistant. Answer in two short sentences.",
    "You are a step-by-step assistant. Give three numbered steps.",
    "You are a customer support assistant. Acknowledge the problem and ask one useful follow-up question."
]

for i, system_message in enumerate(system_messages, start=1):
    response = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction=system_message,
        input=user_question
    )

    print(f"\n--- Experiment {i} ---")
    print(response.output_text)
