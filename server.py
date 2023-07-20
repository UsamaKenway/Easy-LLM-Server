from gradio_.chatbot import ChatBot
import gradio as gr
from fastapi import FastAPI
from LLMApp.core.event_handler import start_app_handler
from LLMApp.api.api import router
import asyncio


class ChatBotApp:
    def __init__(self):
        self.bot = ChatBot()

    def run(self, message, chatbot):
        response = self.bot.respond(message)
        chatbot.append((message, response))
        return "", chatbot


def main():
    app = FastAPI()
    app.add_event_handler("startup", start_app_handler(
        app, "usamakenway/Wizard-Vicuna-7B-Uncensored-SuperHOT-8K-AutoGPTQ"))

    app.include_router(router)

    # Use asyncio event loop to wait for FastAPI server to start
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_fastapi_server(app))


async def start_fastapi_server(app):
    import uvicorn
    config = uvicorn.Config(app, host="0.0.0.0", port=8080, log_level="info")
    server = uvicorn.Server(config)

    # Start the FastAPI server asynchronously
    asyncio.ensure_future(server.serve())

    # Wait for the FastAPI server to be fully running
    while True:
        if server.started:
            break
        await asyncio.sleep(0.1)

    # FastAPI server is running, now start Gradio application
    start_gradio_app()


def start_gradio_app():
    bot_app = ChatBotApp()
    with gr.Blocks() as demo:
        no = gr.Label("LLM WebUI Gradio Server")
        chatbot = gr.Chatbot()

        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(bot_app.run, [msg, chatbot], [msg, chatbot])
    demo.launch(share=True)


if __name__ == "__main__":
    # Run the main function to start both FastAPI and Gradio
    main()


