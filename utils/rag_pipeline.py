import google.generativeai as genai

from utils.prompts import QA_PROMPT, SUMMARY_PROMPT


def generate_answer(context, question):

    prompt = QA_PROMPT.format(
        context=context,
        question=question
    )

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text


def generate_summary(context):

    prompt = SUMMARY_PROMPT.format(
        context=context
    )

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text
