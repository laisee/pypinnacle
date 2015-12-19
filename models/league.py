import json
import time

class League(object):
    """An instance of a League in which games are held

    Attributes:
        id:   ID is league database key
        game_id: id of the Game 
        sport_id: id of the Sport 
        name:  name of the league e.g. "NFL football"
        hometeam: if home team is team1 or team2
        timestamp: unix timestamp(UTC) when sport record was downloaded 
    """

    def __init__(self, id, name, hometeam):
        self.id = id
        self.game_id = 88
        self.name = name
        self.sport_id = 12
        self.hometeam = hometeam
        self.timestamp = int(time.time())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
