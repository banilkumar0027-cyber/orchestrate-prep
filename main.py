
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Send a message
response = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain what an AI agent is in simple words."
)

# Print Gemini's response
print(response.output_text)
