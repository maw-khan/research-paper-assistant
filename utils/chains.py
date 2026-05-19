from google import genai

from utils.prompts import (
    QA_PROMPT,
    SUMMARY_PROMPT
)


def get_gemini_response(api_key, prompt):

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
