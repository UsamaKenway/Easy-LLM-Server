from gradio_.chatbot import ChatBot
import gradio as gr
import threading
import uvicorn


class ChatBotApp:
    def __init__(self):
        self.bot = ChatBot()

    def run(self, message, chatbot):
        response = self.bot.respond(message)
        chatbot.append((message, response))
        return "", chatbot


def run_gradio_server():
    bot_app = ChatBotApp()

    with gr.Blocks() as demo:
        no = gr.Label("LLM WebUI Gradio Server")
        chatbot = gr.Chatbot()

        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(bot_app.run, [msg, chatbot], [msg, chatbot])

    demo.launch(share=True, debug=True)


def run_fastapi_server():
    uvicorn.run("LLMApp.main:app", host="0.0.0.0", port=8080, log_level="info")


if __name__ == "__main__":

    # Start FastAPI server in a separate thread
    fastapi_server_thread = threading.Thread(target=run_fastapi_server)
    fastapi_server_thread.start()

    # Start Gradio server in the main thread
    run_gradio_server()
