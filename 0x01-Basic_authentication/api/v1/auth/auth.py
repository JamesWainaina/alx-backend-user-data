#!/usr/bin/env python3
""" Module of Auth views
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth method
        """

        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                prefix = excluded_path[:-1]
                if normalized_path.startswith(prefix):
                    return False
            elif excluded_path.endswith('/'):
                if normalized_path == excluded_path:
                    return False
            elif normalized_path.endswith(excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header method
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user method
        """
        return None
