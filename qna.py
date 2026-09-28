def answer_question(client, question, context=""):
    prompt = f"""
You are GOKUL AI, a helpful learning assistant.

Answer the student's question clearly and simply.

Student question:
{question}

Additional context:
{context}

Instructions:
- Give a clear and accurate answer.
- Explain difficult ideas in simple language.
- Use an example when helpful.
- Keep the answer student-friendly.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text