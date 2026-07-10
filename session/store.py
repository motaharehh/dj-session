import json
import secrets


class SessionStore:

    def init(self,session):
        self.session = session
        self.data = {}


    def __getitem__(self, key):
        return self.data[key]
