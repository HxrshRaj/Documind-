from dotenv import load_dotenv
import os

load_dotenv()


def get_openai_key():

    return os.getenv(
        "OPENAI_API_KEY"
    )


def get_gemini_key():

    return os.getenv(
        "GEMINI_API_KEY"
    )
def get_groq_key():

    return os.getenv(
        "GROQ_API_KEY"
    )   