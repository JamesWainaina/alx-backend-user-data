#!/usr/bin/env python3

"""
created on July 28, 2024
@ Author: James Gatheru
"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessonExpAuth(SessionAuth):
    """
    class session exp auth
    """

    def __init__(self):
        """Initializes class"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except (ValueError, TypeError):
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        created a session and adds a session ID and creation time to
        super().user_id_by_session_id
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session(self, session_id=None):
        """
        function for creating session_id
        """

        if not session_id:
            return None
        if not self.user_id_by_session_id[session_id]:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)

        user_id = session_dict.get('user_id')
        if self.session_duration <= 0:
            return user_id
        if not session_dict.get('created_at'):
            return None
        created_at = session_dict.get('created_at')
        session_duration = timedelta(seconds=self.session_duration)

        if datetime.now() > (session_duration + created_at):
            return None

        return user_id
