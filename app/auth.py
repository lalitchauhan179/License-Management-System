from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)

# Dummy admin credentials
ADMIN_USER = "admin"
ADMIN_PASS = "adminpassword"

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != ADMIN_USER or not check_password_hash(generate_password_hash(ADMIN_PASS), password):
        return jsonify({"message": "Bad credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
