from fastapi import APIRouter, Request
from LLMApp.langchain.conversation import Conversation
from LLMApp.core.event_handler import _shutdown_model, _startup_model
from LLMApp.utils.core.predict_model import PredictRequest, PredictResponse, LoadModelRequest
from LLMApp.app import app


router = APIRouter()


@router.post("/chat")
async def predict(request: Request, payload: PredictRequest):
    print("API HIT")
    messages = payload.messages
    human_predix = payload.user_name
    ai_prefix = payload.ai_name

    # Get the loaded model instance from the app state
    llm_obj = request.app.state.model_instance

    # Update the stop sequence and get the llm_pipe
    llm_pipe = llm_obj.update_stop_sequence(human_predix)

    chat = Conversation(
        llm_pipe,
        messages=messages,
        ai_prefix=ai_prefix,
        human_prefix=human_predix
    )
    res = chat.predict()

    return PredictResponse(result=res)


@router.post("/unload_model/")
def unload_model():
    try:
        if hasattr(app.state, "model_instance"):
            _shutdown_model(app)
            msg = "Model unloaded successfully"
        else:
            msg = "No model loaded previously"
        return {"message": msg}
    except Exception as e:
        return {"error": str(e)}


@router.post("/load_model/")
def load_model(request: LoadModelRequest):
    model_name = request.model_name
    try:
        _shutdown_model(app)
        _startup_model(app, model_name)
        return {"message": f"Model '{model_name}' loaded successfully."}
    except Exception as e:
        return {"error": str(e)}
