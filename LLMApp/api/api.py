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

    # Get the loaded model instance from the app state
    llm_obj = request.app.state.model_instance

    # Update the stop sequence and get the llm_pipe
    llm_pipe = llm_obj.update_stop_sequence(["\n"+human_predix, "\n"+ai_prefix])

    chat = Conversation(
        llm_pipe,
        messages=messages,
        ai_prefix=ai_prefix,
        human_prefix=human_predix
    )
    res = chat.predict()

    return PredictResponse(result=res)
