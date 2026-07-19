import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_response(prompt: str):

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text


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

    return generate_response(prompt)

def generate_summary(context):

    prompt = f"""
You are an expert research assistant.

Using ONLY the context below, generate a structured summary of the research paper.

Return your answer in the following format:

# Paper Summary

## Objective
(What problem does this paper solve?)

## Methodology
(How did the authors solve the problem?)

## Key Findings
(List the most important findings as bullet points.)

## Conclusion
(Summarize the overall conclusion.)

If any section is not present in the context, mention that it could not be determined.

Context:
{chr(10).join(context)}
"""

    return generate_response(prompt)

def generate_explanation(query, context):

    prompt = f"""
You are an expert teacher.

Using ONLY the context below, explain the user's question in very simple language.

Guidelines:
- Assume the user is a beginner.
- Avoid complex technical jargon.
- Use simple examples or analogies whenever possible.
- Keep the explanation clear and easy to understand.
- If the answer is not found in the context, say:
"I couldn't find this information in the uploaded document."

Context:
{chr(10).join(context)}

Question:
{query}
"""

    return generate_response(prompt)

def generate_contributions(context):

    prompt = f"""
You are an expert research assistant.

Using ONLY the context below, identify the main contributions of this research paper.

Instructions:
- Return only the important contributions.
- Use bullet points.
- Keep each point concise.
- Do not invent information.
- If the contributions cannot be determined, clearly state that.

Context:
{chr(10).join(context)}
"""

    return generate_response(prompt)

def generate_limitations(context):

    prompt = f"""
You are an expert research assistant.

Using ONLY the context below, identify the limitations of this research paper.

Instructions:
- Return the limitations as bullet points.
- Do not invent limitations that are not mentioned.
- If the limitations cannot be determined from the context, clearly state that.

Context:
{chr(10).join(context)}
"""

    return generate_response(prompt)

def generate_future_work(context):

    prompt = f"""
You are an expert research assistant.

Using ONLY the context below, identify the future work or future research directions suggested by the authors.

Instructions:
- Return the future work as bullet points.
- Do not invent information.
- Only include future work that is explicitly mentioned or strongly implied.
- If future work cannot be determined from the context, clearly state that.

Context:
{chr(10).join(context)}
"""

    return generate_response(prompt)    