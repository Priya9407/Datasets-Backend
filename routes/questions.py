from flask import Blueprint, jsonify, request
import os
import json

questions_bp = Blueprint("questions", __name__, url_prefix="/api")

MODULE_NUM_MAP = {
    "cat1": "1",
    "cat2": "2",
    "fat":  "3",
}

@questions_bp.route("/questions", methods=["GET"])
def get_questions():
    course_code = request.args.get("course")
    module = request.args.get("module", "").lower()
    print(course_code)
    if not course_code or module not in MODULE_NUM_MAP:
        return jsonify({"error": "Invalid course or module"}), 400

    # Build the JSON filename dynamically
    json_file = f"{course_code}{MODULE_NUM_MAP[module]}.json"  # e.g., BECE102L1.json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", json_file)

    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        # Return the full JSON (or just questions if you want)
        return jsonify(data), 200

    except FileNotFoundError:
        return jsonify({"error": f"{json_file} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
