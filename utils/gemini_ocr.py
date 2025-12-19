import os
from PIL import Image
from google import genai

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def extract_text_from_image(image_path):
    image = Image.open(image_path)

    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=[
            "Extract all text accurately from the image. "
            "If exam questions exist, return JSON with "
            "question_number, text, difficulty_score.",
            image
        ],
    )

    return response.text
