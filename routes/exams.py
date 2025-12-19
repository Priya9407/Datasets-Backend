from flask import Blueprint, jsonify
import json
import os

exams_bp = Blueprint("exams", __name__, url_prefix="/api")

@exams_bp.route("/exams", methods=["GET"])
def get_exams():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "exams.json")

        with open(json_path, "r") as f:
            data = json.load(f)

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
