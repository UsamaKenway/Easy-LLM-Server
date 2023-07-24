from gradio_.chatbot_app import run_gradio_server
import threading
import uvicorn


def run_fastapi_server():
    uvicorn.run("LLMApp.main:app", host="0.0.0.0", port=8080, log_level="info")


if __name__ == "__main__":
    # Start FastAPI server in a separate thread
    fastapi_server_thread = threading.Thread(target=run_fastapi_server)
    fastapi_server_thread.start()

    # Start Gradio server in the main thread
    run_gradio_server()
