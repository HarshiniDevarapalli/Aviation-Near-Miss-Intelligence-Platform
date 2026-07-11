from google import genai

from src.config import GEMINI_MODEL


class GeminiService:
    """
    Handles communication with the Gemini API.
    """

    def __init__(self, api_key: str):

        if not api_key:
            raise ValueError(
                "Gemini API key not found."
            )

        self.client = genai.Client(api_key=api_key)

        print("Gemini client initialized successfully!")

    def generate_report(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"Gemini Error: {e}"