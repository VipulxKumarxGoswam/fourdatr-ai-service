import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.text import router as text_router
from app.routes.image import router as image_router
from app.routes.rewrite import router as rewrite_router

app = FastAPI(
    title="Variseocisk AI Service",
    description="AI Backend for Variseocisk",
    version="1.0.0"
)

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Serve generated images
app.mount("/images", StaticFiles(directory="outputs"), name="images")


@app.get("/")
def home():
    return {
        "message": "Welcome to Variseocisk AI Service"
    }


@app.get("/health")
def health():
    return {
        "status": "Running",
        "service": "Variseocisk AI"
    }


# Register Routes
app.include_router(text_router)
app.include_router(image_router)
app.include_router(rewrite_router)