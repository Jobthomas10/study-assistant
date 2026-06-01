from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

personalities = {
    "Friendly":
    "You are a friendly, enthusiastic tutor. Explain concepts simply using examples and analogies. Ask a follow-up question.",

    "Academic":
    "You are a professional university professor. Give detailed and structured explanations with formal terminology."
}

def study_assistant(question, persona):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=personalities[persona],
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=question
    )
    return response.text

question = input("Enter your question: ")
personality = input("Choose personality (Friendly/Academic): ")

print("\nResponse:\n")
print(study_assistant(question, personality))