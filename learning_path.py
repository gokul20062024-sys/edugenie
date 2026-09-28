def create_learning_path(client, topic):
    prompt = f"""
Create a structured learning path for a student who wants to learn:

Topic: {topic}

Organize the learning path into 5 stages:
1. Beginner basics
2. Fundamental concepts
3. Intermediate concepts
4. Advanced concepts
5. Practice and projects

For each stage:
- Give a clear stage title
- List the important topics to study
- Suggest a small practice activity

Keep it simple, practical, and student-friendly.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text