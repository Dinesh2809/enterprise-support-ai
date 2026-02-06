from google import genai
from configs.settings import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def classify_intent(ticket_text: str) -> str:
    """
    Classify support ticket into predefined intent categories.
    """

    prompt = f"""
You are an enterprise support ticket classifier.

Classify the user ticket into ONE of these categories:
- login_issue
- payment_problem
- bug_report
- feature_request
- other

Return ONLY the category name.

Ticket:
{ticket_text}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text.strip()
