import chainlit as cl
import requests
from config import API_KEY, API_URL, MODEL

# Store conversation history
history = []

def query_llm(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost"  # Required by OpenRouter
    }

    payload = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"[ERROR] {response.status_code}: {response.text}"

@cl.on_message
async def main(message: cl.Message):
    user_msg = {"role": "user", "content": message.content}
    history.append(user_msg)

    # Call LLM
    response = query_llm(history)

    # Add assistant message to history
    history.append({"role": "assistant", "content": response})

    # Send reply to UI
    await cl.Message(content=response).send()
