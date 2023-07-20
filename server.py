import gradio as gr
import random
import time
from gradio.chatbot import ChatBot


class ChatBotApp:
    def __init__(self):
        self.bot = ChatBot()

    def run(self, message, chatbot):
        response = self.bot.respond(message)
        chatbot.append((message, response))
        return "", chatbot


if __name__ == "__main__":
    bot_app = ChatBotApp()

    with gr.Blocks() as demo:
        no = gr.Label("title here")
        chatbot = gr.Chatbot()

        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(bot_app.run, [msg, chatbot], [msg, chatbot])

    demo.launch(share=True)