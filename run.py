from openai import OpenAI
import pytest
client = OpenAI()

def generate_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="o3-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
