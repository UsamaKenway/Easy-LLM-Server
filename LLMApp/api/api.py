from fastapi import APIRouter, Request
from LLMApp.langchain.conversation import Conversation
from LLMApp.utils.core.predict_model import PredictRequest, PredictResponse

router = APIRouter()


@router.post("/chat")
async def predict(request: Request, payload: PredictRequest):
    print("API HIT")
    messages = payload.messages
    human_predix = payload.user_name
    ai_prefix = payload.ai_name
    chat = Conversation(
        request.app.state.model_instance,
        messages=messages,
        ai_prefix=ai_prefix,
        human_prefix=human_predix
    )
    res = chat.predict()

    return PredictResponse(result=res)
