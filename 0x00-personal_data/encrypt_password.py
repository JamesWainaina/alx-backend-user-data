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
