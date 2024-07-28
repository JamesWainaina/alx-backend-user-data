#!/usr/bin/env python3
"""
created at July 28 2024
Author @ James Gatheru
"""

from api.v1.views import app_views
from flask import request
from models.user import User
from flask import abort, jsonify, request
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """
    POST /api/v1/auth_session/login function
    """
    user_email = request.form.get('email')

    if user_email is None:
        return jsonify({"error": "email missing"}), 400

    user_password = request.form.get('password')

    if user_password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': user_email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(user_password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            cookie = getenv('SESSION_NAME')
            response = jsonify(user.to_json())
            response.set_cookie(cookie, session_id)

            return response
    return jsonify({"error": "wrong password"}), 401
