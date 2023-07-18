from typing import Callable
from fastapi import FastAPI
from LLMApp.models.auto_gptq import GPTQModel
import torch


def _startup_model(app: FastAPI, model_name: str) -> None:
    app.state.model_instance = GPTQModel(model_name).load_model()


def start_app_handler(app: FastAPI, model_name: str) -> Callable:
    def startup() -> None:
        _startup_model(app, model_name)
    return startup
