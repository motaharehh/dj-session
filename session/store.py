import json
import secrets


class SessionStore:

    def init(self,session):
        self.session = session
        self.data = {}


    def __getitem__(self, key):
        return self.data[key]
    

    def __setitem__(self, key, value):
        self.data[key] = value


    