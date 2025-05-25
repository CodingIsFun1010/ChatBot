# app.py

import openai
from flask import Flask, request, jsonify
import os

# Initialize the Flask app
app = Flask(__name__)

# Set up OpenAI API Key (replace with your own API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Make sure to set your OpenAI API key here!

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided!"}), 400

    try:
        # Request a response from OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",  # Use the GPT-3 or GPT-4 model
            prompt=user_message,
            max_tokens=150,
            temperature=0.9,
            n=1,
            stop=None
        )
        
        # Get the model's response
        chatbot_reply = response.choices[0].text.strip()

        return jsonify({"response": chatbot_reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
