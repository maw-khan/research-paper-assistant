from google import genai

from utils.prompts import (
    QA_PROMPT,
    SUMMARY_PROMPT
)


def get_gemini_response(api_key, prompt):

    client = genai.Client(api_key=api_key)
    response_bool=False

    try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    response_bool=True
    return response.text,response_bool

    except Exception as e:
    
        error_message = str(e)
    
    return error_message,response_bool

