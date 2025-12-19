from flask import Blueprint, jsonify
import json
import os

subjects_bp = Blueprint("subjects", __name__, url_prefix="/api")

@subjects_bp.route("/subjects", methods=["GET"])
def get_subjects():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "subjects.json")
    print(json_path)
    with open(json_path, "r") as f:
        data = json.load(f)

    return jsonify(data)
