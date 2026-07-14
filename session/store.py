import json
import secrets


class SessionStore:

    def __init__(self, session):
        
        self.session = session
        if session.session_data:
            self.data = json.loads(session.session_data)
        else:
            self.data = {}


    def __getitem__(self, key):
        return self.data[key]
    

    def __setitem__(self, key, value):
        self.data[key] = value


    def save(self):
        self.session.session_data = json.dumps(self.data)
        self.session.save()

    def __contains__(self, key):
        return key in self.data
    
    def cycle_key(self):
        pass