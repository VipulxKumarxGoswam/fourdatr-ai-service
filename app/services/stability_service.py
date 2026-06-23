import os
import time
import requests
from app.config import STABILITY_API_KEY


def generate_image(prompt: str):

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Accept": "image/*"
    }

    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png")
    }

    response = requests.post(
        url,
        headers=headers,
        files=files
    )

    if response.status_code != 200:
        raise Exception(response.text)

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Generate unique filename using current timestamp
    filename = f"generated_{int(time.time())}.png"

    # Full file path
    image_path = os.path.join("outputs", filename)

    # Save image
    with open(image_path, "wb") as f:
        f.write(response.content)

    # Return only the filename
    return filename