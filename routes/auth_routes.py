from flask import Blueprint, request, jsonify, current_app
from models.user_model import find_user_by_email, create_user
from utils.security import hash_password

import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Fix: Pass the current_app.db to find_user_by_email
    if find_user_by_email(email, current_app.db):
        return jsonify({'error': 'User already exists'}), 409

    hashed_pw = hash_password(password)

    # Fix: Pass the current_app.db to create_user
    create_user(email, hashed_pw, current_app.db)

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Fix: Use current_app.db to get user
    db = current_app.db
    user = db.users.find_one({"email": email})

    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    stored_password = user.get("password")
    # Fix: Ensure password is bytes for bcrypt.checkpw
    if isinstance(stored_password, str):
        stored_password = stored_password.encode("utf-8")

    if not bcrypt.checkpw(password.encode("utf-8"), stored_password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Login successful"}), 200
