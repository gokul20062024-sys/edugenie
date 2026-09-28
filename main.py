from flask import Flask, render_template, request, jsonify
from google import genai
from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from learning_path import create_learning_path
from summary_module import generate_summary
import os
from explanation_module import explain_topic

app = Flask(__name__)

# Gemini setup
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.5-flash-lite"


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "Please enter a topic."}), 400

    try:
        explanation = explain_topic(client, topic)

        return jsonify({
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
@app.route("/quiz", methods=["POST"])
def quiz():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "Please enter a topic."}), 400

    try:
        quiz = generate_quiz(client, topic)

        return jsonify({
            "quiz": quiz
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
@app.route("/learning-path", methods=["POST"])
def learning_path():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "Please enter a topic."}), 400

    try:
        path = create_learning_path(client, topic)

        return jsonify({
            "learning_path": path
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
@app.route("/summary", methods=["POST"])
def summary():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "Please enter a topic."}), 400

    try:
        summary = generate_summary(client, topic)

        return jsonify({
            "summary": summary
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    models = [
        "gemini-3.5-flash-lite",
        "gemini-3.6-flash",
        "gemini-3.7-flash"
    ]

    for model in models:
        try:
            answer = answer_question(client, question)
            

            return jsonify({
                "answer": answer,
                "model": model
            })

        except Exception as e:
            print(f"{model} failed: {e}")
            continue

    return jsonify({
        "error": "Gemini is temporarily unavailable. Please try again in a few seconds."
    }), 503


if __name__ == "__main__":
    app.run(debug=True)