from utils.config import (
    get_groq_key
)

from agents.groq_agent import (
    enhance_knowledge
)

api_key = get_groq_key()

response = enhance_knowledge(

    "Classification uses Logistic Regression and Random Forest.",

    "Classification",

    api_key
)

print(response)