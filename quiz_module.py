def generate_quiz(client, topic):
    prompt = f"""
Create a short quiz for a student learning about:

Topic: {topic}

Create 5 multiple-choice questions.

For each question include:
1. The question
2. Four options labeled A, B, C, and D
3. The correct answer
4. A one-line explanation of the answer

Keep the questions clear and suitable for a student.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text