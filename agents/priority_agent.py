from google import genai
from configs.settings import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def detect_priority(ticket_text: str) -> str:
    """
    Classify ticket urgency into: high, medium, low
    """

    prompt = f"""
You are an enterprise support triage system.

Classify the PRIORITY of this support ticket into ONE of:
- high
- medium
- low

Rules:
- Production down, payment failure → high
- Feature not working → medium
- General query → low

Return ONLY the priority word.

Ticket:
{ticket_text}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text.strip().lower()
