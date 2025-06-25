import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.mistral.ai/v1/chat/completions"


MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def call_mistral(text):
    import requests
    import os

    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise Exception("API key not loaded. Please check .env or environment variables.")

    prompt = f"""
Extract semantic metadata from the following document content.

{text}

Return only a raw JSON object like this (no explanation, no markdown, no text outside JSON):

{{
  "title": "...",
  "summary": "...",
  "keywords": "...",
  "main_topics": "...",
  "document_type": "...",
  "text_length_in_characters": ...
}}
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistral-medium",  # or the model you are using
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json=body
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
