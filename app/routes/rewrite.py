from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemini_service import rewrite_text

router = APIRouter()


class RewriteRequest(BaseModel):
    text: str
    action: str


@router.post("/rewrite-text")
def rewrite(request: RewriteRequest):

    result = rewrite_text(
        request.text,
        request.action
    )

    return {
        "success": True,
        "text": result
    }