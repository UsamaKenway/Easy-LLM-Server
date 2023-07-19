from pydantic import BaseModel, Field, StrictStr
from typing import Optional, List, Dict


class PredictRequest(BaseModel):
    user_name: Optional[str] = Field("Human", title="user_name",
                                     description="User's name")
    ai_name: Optional[str] = Field("AI", title="ai_name", description="AI's name")
    messages: List[Dict[str, str]] = Field(..., title="data_dictionary",
                                           description="Data dictionary")


class PredictResponse(BaseModel):
    result: str = Field(..., title="result", description="Text")
