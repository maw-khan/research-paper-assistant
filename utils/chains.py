from google import genai

from utils.prompts import (
    QA_PROMPT,
    SUMMARY_PROMPT
)


def get_gemini_response(api_key, prompt):

    try:

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        error_message = str(e)

        # Gemini overloaded
        if "503" in error_message or "high demand" in error_message.lower():

            return (
                "⚠️ Gemini API is currently experiencing high demand.\n\n"
                "Please wait a few moments and try again."
            )

        # Generic error
        return (
            "⚠️ Unable to generate response right now.\n\n"
            "Please try again later."
        )
