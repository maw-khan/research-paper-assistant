from google import genai

from utils.prompts import (
    QA_PROMPT,
    SUMMARY_PROMPT
)


from google import genai
import streamlit as st


def get_gemini_response(api_key, prompt):

    try:

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    # =========================
    # QUOTA EXCEEDED (429)
    # =========================

    except Exception as e:

        error_message = str(e)

        # Free tier quota exceeded
        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:

            st.warning(
                "⚠️ Gemini free-tier quota exceeded. "
                "Please wait a while or try again later."
            )

            return None

        # High demand / overloaded servers
        elif "503" in error_message or "UNAVAILABLE" in error_message:

            st.warning(
                "⚠️ Gemini servers are currently busy. "
                "Please retry in a few moments."
            )

            return None

        # Invalid API key
        elif "API key not valid" in error_message:

            st.warning(
                "⚠️ Invalid Gemini API key."
            )

            return None

        # Generic fallback
        else:

            st.warning(
                "⚠️ An unexpected Gemini API error occurred."
            )

            return None
