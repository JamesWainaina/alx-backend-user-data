#!/usr/bin/env python3

"""
Hashing passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    function for hashing passwords using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function for validating hashed password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
