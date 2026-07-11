import os
from dotenv import load_dotenv
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
from src.prompts import build_prompt
from src.gemini_service import GeminiService

load_dotenv()

service = GeminiService(
    os.getenv("GEMINI_API_KEY")
)

prompt = build_prompt(
    "Aircraft taxiing in dense fog",
    "Test context"
)

response = service.generate_report(
    prompt
)

print(response)