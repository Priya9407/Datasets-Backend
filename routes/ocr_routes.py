import os
from flask import Blueprint, request, jsonify
from utils.gemini_ocr import extract_text_from_image

ocr_bp = Blueprint("ocr", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@ocr_bp.route("/ocr", methods=["POST"])
def ocr():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    text = extract_text_from_image(image_path)
    return jsonify({"result": text})
