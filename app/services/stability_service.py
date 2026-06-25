import os
import time

from huggingface_hub import InferenceClient
from app.config import HUGGINGFACE_API_KEY


def generate_image(prompt: str):

    try:

        client = InferenceClient(
            api_key=HUGGINGFACE_API_KEY
        )

        image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )

        # Create outputs folder
        os.makedirs("outputs", exist_ok=True)

        # Unique filename
        filename = f"generated_{int(time.time())}.png"

        # Full path
        image_path = os.path.join("outputs", filename)

        # Save image
        image.save(image_path)

        print("Image saved successfully:", image_path)

        return filename

    except Exception as e:

        print("IMAGE GENERATION ERROR:", str(e))

        raise Exception(str(e))