from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_with_ai(log_text):
    prompt = f"""
    You are a senior SRE.

    Return ONLY valid JSON.
    Do NOT use markdown.
    Do NOT wrap in backticks.
    Do NOT include explanation.

    Schema:
    {{
      "major_issues": [],
      "recurring_failures": [],
      "root_causes": [],
      "recommendations": []
    }}

    Logs:
    {log_text}
    """
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content