import json
import time

class Match(object):
    """An instance of a Match betweem 2 teams 

    Attributes:
        id:   ID is match database key
        start: date/time match is scheduled to start
        team1: home team if league.hometeam is team1 
        team2: home team if league.hometeam is team2
        league: league in which match is played
        timestamp: unix timestamp(UTC) when record was downloaded 
    """

    def __init__(self, id, start, team1, team2, league=None):
        self.id = id
        self.start = start
        self.team1 = team1
        self.team2 = team2
        self.league = league
        self.timestamp = int(time.time())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
