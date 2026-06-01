from utils.config import (
    get_gemini_key
)

from agents.gemini_agent import (
    enhance_knowledge
)

api_key = get_gemini_key()

response = enhance_knowledge(
    "Classification uses Logistic Regression and Random Forest.",
    "Classification",
    api_key
)

print(response)