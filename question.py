import os
import time
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Read API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Question generator function
def question_generator(user_prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# User input
text = input("Enter the text:\n")


prompt = f"""
Answer the following question in a natural, human-like way.

Guidelines:
- Use simple and conversational language.
- Sound like a real person explaining something.
- Avoid robotic or AI-style phrases.
- Be clear and concise.
- Give practical examples when helpful.

Question:


{text}
"""

# Retry loop
while True:
    result = question_generator(prompt)

    if "429" in result:
        print("Rate limit reached. Waiting 30 seconds...\n")
        time.sleep(30)
    else:
        print("\nGenerated Questions:\n")
        print(result)
        break