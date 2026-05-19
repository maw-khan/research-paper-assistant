from google import genai

from utils.prompts import (
    QA_PROMPT,
    SUMMARY_PROMPT
)


def get_gemini_response(api_key, prompt):

    client = genai.Client(api_key=api_key)

    try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    except Exception as e:
    
        error_message = str(e)
    
        if "503" in error_message or "high demand" in error_message.lower():
    
            st.warning(
                "⚠️ Gemini API is currently experiencing high demand. "
                "Please wait a few moments and try again."
            )
    
        else:
    
            st.warning(
                "⚠️ Unable to generate response at the moment. "
                "Please try again."
            )
    
        st.stop()
    return response.text
