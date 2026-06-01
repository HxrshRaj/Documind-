from groq import Groq


def enhance_knowledge(
    retrieved_context,
    task,
    api_key
):

    client = Groq(
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

Keep the response concise.
"""

    response = client.chat.completions.create(

        model=
        "llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )