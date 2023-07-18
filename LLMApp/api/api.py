from fastapi import APIRouter
from pydantic import BaseModel, Field, StrictStr
from typing import Optional, List, Dict

router = APIRouter()


class PredictRequest(BaseModel):
    user_name: Optional[str] = Field(None, title="user_name", description="User's name")
    ai_name: Optional[str] = Field(None)
    messages: List[Dict[str, str]] = Field(..., title="data_dictionary",
                                          description="Data dictionary")


@router.post("/chat")
async def predict(payload: PredictRequest):
    messages = payload.messages
    human_predix = payload.user_name
    ai_prefix = payload.ai_name

    return {"result": "success"}
