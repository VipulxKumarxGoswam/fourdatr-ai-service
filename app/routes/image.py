from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from app.services.stability_service import generate_image

router = APIRouter()


class ImageRequest(BaseModel):
    prompt: str


@router.post("/generate-image")
def image(request: ImageRequest, req: Request):

    try:

        # Generate image and get filename
        filename = generate_image(request.prompt)

        # Build full URL
        base_url = str(req.base_url).rstrip("/")
        image_url = f"{base_url}/images/{filename}"

        return {
            "success": True,
            "imageUrl": image_url
        }

    except Exception as e:

        print("IMAGE ROUTE ERROR:", str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )