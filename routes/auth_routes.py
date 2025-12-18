from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from utils.password import hash_password, verify_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "User already exists"}), 409

    user = User(
        name=data.get("name"),
        email=data["email"],
        phone=data.get("phone"),
        institution=data.get("institution"),
        department=data.get("department"),
        year=data.get("year"),
        roll_number=data.get("rollNumber"),
        password=hash_password(data["password"]),
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not verify_password(user.password, data["password"]):
        return jsonify({"msg": "Invalid email or password"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({
        "access_token": token,
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    })
