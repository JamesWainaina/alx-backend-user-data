#!/usr/bin/env python3

"""
created on Sat Jul 11:55 2024
@Author: James Gatheru
"""
from api.v1.auth.auth import Auth


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
