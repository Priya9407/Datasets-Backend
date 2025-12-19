from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from services.ocr import extract_text_from_image

answer_bp = Blueprint("answer", __name__, url_prefix="/api")

UPLOAD_FOLDER = "uploads/answers"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@answer_bp.route("/submit-answer", methods=["POST"])
def submit_answer():
    answer_text = request.form.get("answer_text")
    question_id = request.form.get("question_id")

    file = request.files.get("image")

    extracted_text = None

    if file:
        filename = secure_filename(file.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(image_path)

        extracted_text = extract_text_from_image(image_path)

    return jsonify({
        "question_id": question_id,
        "typed_answer": answer_text,
        "extracted_text": extracted_text,
        "feedback": "Answer received successfully. AI evaluation coming next."
    })
