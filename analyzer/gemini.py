import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("NEW_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

def get_ai_feedback(resume_text):

    prompt = f"""
    Analyze this resume and provide:

    1. Strengths
    2. Weaknesses
    3. Missing Skills
    4. Improvement Suggestions

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text
