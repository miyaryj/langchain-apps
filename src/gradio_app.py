import gradio as gr
from dotenv import load_dotenv
from chatbot_engine import chat
from langchain.memory import ChatMessageHistory
import os


def respond(message, chat_history):
    print(chat_history)
    history = ChatMessageHistory()
    for [user_message, ai_message] in chat_history:
        history.add_user_message(user_message)
        history.add_ai_message(ai_message)
    return chat(message, history)

if __name__ == "__main__":
    load_dotenv()

    app_env = os.environ.get("APP_ENV", "production")
    if app_env == "production":
        username = os.environ["GRADIO_USERNAME"]
        password = os.environ["GRADIO_PASSWORD"]
        auth = (username, password)
    else:
        auth = None

    gr.ChatInterface(respond).launch(auth=auth)