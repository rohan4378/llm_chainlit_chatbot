 LLM Chatbot with Chainlit

This project is a conversational chatbot powered by a **Large Language Model (LLM)** and built using **Chainlit** — a Python framework that allows easy deployment of interactive AI apps. It uses an external LLM API (like OpenAI) to generate intelligent responses based on user queries.

--- Features

-  Connected to an LLM via API (e.g., OpenAI)
-  Remembers previous messages for better context
- Real-time user interface with Chainlit
-  Easy to customize or extend with other data sources (RAG-ready)

---

 Project Structure

llm-chatbot/
│
├── main.py # Main Chainlit app handling input/output
├── config.py # API keys, model configuration
├── requirements.txt # Python dependencies
├── .env # Optional: Secure storage for API keys
└── README.md # Project documentation

yaml
Copy
Edit

---

 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/llm-chatbot.git
cd llm-chatbot
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set your API key
You can store it in config.py:

python
Copy
Edit
API_KEY = "your_api_key"
API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-3.5-turbo"
Or use an .env file and os.getenv() to keep it secure.

▶️ Running the Chatbot
Start the Chainlit app locally:

bash
Copy
Edit
chainlit run main.py
Then open the browser at the local URL provided (e.g., http://localhost:8000).

🧠 How It Works
User types a message in the Chainlit interface.

The message and prior chat history are sent to the external LLM API.

The model generates a response based on the input + context.

The chatbot displays the response in the same interface.

 Tech Stack
Python 3.10+

Chainlit – UI + interaction layer

LLM API – e.g., OpenAI or any compatible hosted model

Requests – To send API calls

 Example
python
Copy
Edit
# main.py (core logic)
import chainlit as cl
import requests
from config import API_KEY, MODEL, API_URL

conversation_history = []

@cl.on_message
def handle_user_message(message):
    conversation_history.append({"role": "user", "content": message.content})

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": conversation_history
        }
    )

    reply = response.json()["choices"][0]["message"]["content"]
    conversation_history.append({"role": "assistant", "content": reply})

    cl.Message(content=reply).send()

💡 Future Improvements
Add PDF upload + context-aware answers (RAG)

Add voice support using Speech-to-Text

Add chat session persistence

Deploy via Docker, Streamlit, or Hugging Face Spaces

Author
Rohan Kapila
B.Tech in IoT (CSE) | Deep Learning & AI Enthusiast
LinkedIn

 License
MIT License — free to use, modify, and share.