import json
import time

class Sport(object):
    """An instance of a game for which schedules and bets are managed and displayed

    Attributes:
        id:   ID is sports database key
        name:  name of the game e.g. "football"
        timestamp: unix timestamp(UTC) when sport record was downloaded 
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.timestamp = int(time.time())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
