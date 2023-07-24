from gradio_.chatbot import ChatBot
import gradio as gr


class ChatBotApp:
    def __init__(self):
        self.bot = ChatBot()

    def run(self, message, chatbot):
        """
        Runs the chatbot with the provided user message, updating the chatbot's response.

        Args:
            message (str): The user's message to send to the chatbot.
            chatbot (list): A list containing the conversation history
            (tuples of user message and bot response). # In Gradio format

        Returns:
            tuple: An empty tuple along with the updated chatbot list.
        """
        response = self.bot.respond(message)
        chatbot.append((message, response))
        return "", chatbot

    def update_prompt(self, prompt):
        self.bot.update_system_messages(prompt)


def run_gradio_server():
    """
    Runs the Gradio server for the chatbot application.
    """
    bot_app = ChatBotApp()

    with gr.Blocks() as demo:
        no = gr.Label("LLM WebUI Gradio Server")
        gr.Interface(fn=bot_app.update_prompt, inputs="text", outputs=None)

        chatbot = gr.Chatbot()

        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(bot_app.run, [msg, chatbot], [msg, chatbot])

    demo.launch(share=True, debug=True)
