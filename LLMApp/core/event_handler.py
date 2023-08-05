from typing import Callable
from fastapi import FastAPI
from LLMApp.models.load_llm import GPTQModel, HFModel
import torch


def _startup_model(app: FastAPI, model_name: str) -> None:
    app.state.model_instance = HFModel(model_name)
    app.state.model_instance.load_model()


def start_app_handler(app: FastAPI, model_name: str) -> Callable:
    def startup() -> None:
        _startup_model(app, model_name)
    return startup
