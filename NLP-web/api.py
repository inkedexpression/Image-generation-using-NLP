from huggingface_hub import InferenceClient
from PIL import Image
import io

def img_gen(text):
    client = InferenceClient(
        model="black-forest-labs/FLUX.1-dev",
        token="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"
    )

    # Generate image from text
    image = client.text_to_image(text)

    # Save the image locally in the 'static' folder
    image_path = "static/generated_image.png"
    image.save(image_path)

    return image_path