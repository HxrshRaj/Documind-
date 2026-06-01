from google import genai


def enhance_knowledge(
    retrieved_context,
    task,
    api_key
):

    client = genai.Client(
        api_key=api_key
    )

    prompt = f"""
You are a Senior Data Science Expert.

Task:
{task}

Retrieved Knowledge:
{retrieved_context}

Provide:

1. Key Takeaways
2. Best Practices
3. Model Selection Advice
4. Deployment Considerations

Keep the response concise and practical.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text