class igame_state(object):
    LOGIN = 0
    CONNECTED = 99
    MISSION = 100
    MISSION_SUCCESS = 200
    CONNECTION_LOST = 404
    UNDEFINE = -1
    STATE = None
    def __init__(self, *args, **kwargs):
        return super(igame_state, self).__init__(*args, **kwargs)
    def state(self):
        pass
class idmm_game(object):
    """description of class"""
    def __init__(self, *args, **kwargs):
        return super(idmm_game, self).__init__(*args, **kwargs)
    def login(self):
        pass
    def start(self):
        pass
    def state(self):
        pass

