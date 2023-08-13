from typing import Callable
from fastapi import FastAPI
from LLMApp.models.load_llm import GPTQModel, HFModel
import torch
import time
import gc


def _startup_model(app: FastAPI, model_name: str) -> None:
    app.state.model_instance = HFModel(model_name)
    app.state.model_instance.load_model()


def _shutdown_model(app: FastAPI) -> None:
    if hasattr(app.state, "model_instance"):
        del app.state.model_instance
        print("Unloading Model")
        time.sleep(5)
        gc.collect()
        torch.cuda.empty_cache()
        print("Model Unloaded")


def start_app_handler(app: FastAPI, model_name: str) -> Callable:
    def startup() -> None:
        _startup_model(app, model_name)
    return startup


def shutdown_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)
    return shutdown
