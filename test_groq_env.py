# test_groq_env.py

from dotenv import load_dotenv
import os

load_dotenv()

print(
    "FOUND"
    if os.getenv("GROQ_API_KEY")
    else "NOT FOUND"
)