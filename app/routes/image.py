from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.services.stability_service import generate_image

router = APIRouter()


class ImageRequest(BaseModel):
    prompt: str


@router.post("/generate-image")
def image(request: ImageRequest, req: Request):

    # Generate image and get filename
    filename = generate_image(request.prompt)

    # Build the full URL dynamically
    base_url = str(req.base_url).rstrip("/")
    image_url = f"{base_url}/images/{filename}"

    return {
        "success": True,
        "imageUrl": image_url
    }