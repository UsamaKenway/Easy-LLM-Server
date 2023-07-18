from fastapi import APIRouter

router = APIRouter()


@router.get("/items/")
async def predict(payload: dict):
    return {"result": "success"}
