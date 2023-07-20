from fastapi import FastAPI
from LLMApp.core.event_handler import start_app_handler
from LLMApp.api.api import router
app = FastAPI()

app.add_event_handler("startup", start_app_handler(
    app, "usamakenway/Wizard-Vicuna-7B-Uncensored-SuperHOT-8K-AutoGPTQ"))

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")