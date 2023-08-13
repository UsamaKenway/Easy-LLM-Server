from fastapi import FastAPI
from LLMApp.core.event_handler import start_app_handler, shutdown_app_handler
from LLMApp.api.api import router
from LLMApp.app import app

# app = FastAPI()

app.add_event_handler("startup", start_app_handler(
    app, "abhishek/llama-2-7b-hf-small-shards"))
app.add_event_handler("shutdown", shutdown_app_handler(app))

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
