import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(query, context):

    prompt = f"""
You are a helpful research assistant.

Answer the user's question using ONLY the context below.

If the answer is not present in the context, clearly say:
"I couldn't find this information in the uploaded document."

Context:
{chr(10).join(context)}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text