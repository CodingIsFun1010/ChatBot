# Unrestricted AI Chatbot

This is a simple Python-based chatbot using OpenAI's GPT model. You can send any message to the chatbot and get a response, similar to ChatGPT.

## Prerequisites

- Python 3.7 or later
- An OpenAI API key (You can get one from [OpenAI](https://beta.openai.com/signup/))

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/unrestricted-chatbot.git
    cd unrestricted-chatbot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    - In `app.py`, replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key.

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to interact with the chatbot.

## How to Use

- Send a POST request to `http://127.0.0.1:5000/chat` with a JSON body:
  
  ```json
  {
      "message": "Your message here"
  }
