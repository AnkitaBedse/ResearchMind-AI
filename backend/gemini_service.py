import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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

    response = model.generate_content(prompt)

    return response.text