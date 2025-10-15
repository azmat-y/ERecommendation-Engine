from ..config import settings
from google import generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)


def explain_recommendation(
    user_id: int, product_name: str, behavior_summary: str
) -> str:
    prompt = f"""
    You are an e-commerce assistant. Explain in a friendly tone why the product \"{product_name}\" was recommended.
    User behavior summary:
    {behavior_summary}
    Keep it concise (3–5 sentences).
    """
    model = genai.GenerativeModel(settings.LLM_MODEL)
    response = model.generate_content(prompt)
    return response.text.strip()
