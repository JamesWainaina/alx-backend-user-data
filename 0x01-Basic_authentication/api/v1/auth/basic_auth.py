#!/usr/bin/env python3

"""
created on Sat Jul 11:55 2024
@Author: James Gatheru
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Basic Authentication class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        function that returns the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        function that returns the decoded value of Base64 string
        """

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decode_base64_authorization_header: str) -> (str, str):
        """
        function that returns the user email and password
        from base64 decoded value
        """

        if decode_base64_authorization_header is None:
            return None, None

        if not isinstance(decode_base64_authorization_header, str):
            return None, None

        if ':' not in decode_base64_authorization_header:
            return None, None

        user, password = decode_base64_authorization_header.split(':', 1)

        return user, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Function that returns the User instance
        based on his email and password
        """
        if user_email is None or user_pwd is None:
            return None

        if not isinstance(user_email, str):
            return None
        if not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
