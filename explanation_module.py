def explain_topic(client, topic):
    prompt = f"""
Explain the following topic to a student in a simple and easy-to-understand way:

Topic: {topic}

Include:
1. A simple definition
2. How it works
3. A small example
4. Important points to remember
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text