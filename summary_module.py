def generate_summary(client, topic):
    prompt = f"""
Create a simple and clear study summary for a student learning about:

Topic: {topic}

Include:
1. A short introduction
2. The main concepts
3. Important points to remember
4. A simple example
5. A short final recap

Use simple language and organize the summary with headings and bullet points.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text