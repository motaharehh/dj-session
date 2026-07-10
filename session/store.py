import json
import secrets


class SessionStore:

    def init(self,session):
        self.session = session
        self.data = {}
        