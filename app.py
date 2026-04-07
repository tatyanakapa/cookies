from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY")

# Храним историю диалога (упрощённо)
chat_history = []

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    chat_history.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Ты — специалист поддержки интернет-магазина. Отвечай кратко и по делу."}
        ] + chat_history
    )

    answer = response.choices[0].message.content

    chat_history.append({"role": "assistant", "content": answer})

    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
