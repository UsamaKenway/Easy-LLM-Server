from fastapi import APIRouter, Request
from pydantic import BaseModel, Field, StrictStr
from typing import Optional, List, Dict
from LLMApp.langchain.conversation import Conversation

router = APIRouter()


class PredictRequest(BaseModel):
    user_name: Optional[str] = Field(None, title="user_name", description="User's name")
    ai_name: Optional[str] = Field(None)
    messages: List[Dict[str, str]] = Field(..., title="data_dictionary",
                                          description="Data dictionary")


@router.post("/chat")
async def predict(request: Request, payload: PredictRequest):
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

    return {"result": res}
