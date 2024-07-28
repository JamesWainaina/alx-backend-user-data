#!/usr/bin/env python3

"""
created on July 28 2024
Author @ James Gatheru
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session for a User
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_Id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[session_Id] = user_id

        return session_Id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID
        """

        if session_id is None or not isinstance(session_id, str):
            return None

        return self.__class__.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """(overload) method that returns a User instance
        based on the cookie value
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
    
    def destroy_session(self, request=None):
        """
        Function for destroying a session
        """

        if request is None:
            return False
    
        if not self.session_cookie(request):
            return False
    
        session_id = self.session_cookie(request)
        if not self.user_id_for_session_id(session_id):
            return False
    
        del self.__class__.user_id_by_session_id[session_id]
        return True
