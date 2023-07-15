from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Initialize chat history with an empty list
chat_history = []


@app.route("/", methods=["GET", "POST"])
def chat():
  if request.method == "POST":
    user_input = request.form.get("user_input")

    # Add user input to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Generate AI response
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=chat_history)
    ai_response = response.choices[0].message.content

    # Add AI response to chat history
    chat_history.append({"role": "assistant", "content": ai_response})

  return render_template("chat.html", chat_history=chat_history)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
