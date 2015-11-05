import json
import time

class Odds(object):
    """An instance of an Odds record for a Match

    Attributes:
        id:   ID is oods database key (generated)
        team1_odds: home team odds
        team2_odds: home team odds
        event_id: event id of the Match on which odds are quoted 
        timestamp: unix timestamp(UTC) when record was downloaded 
    """

    def __init__(self, team1_odds, team2_odds, event_id):
        self.team1_odds = team1_odds
        self.team2_odds = team2_odds
        self.event_id = event_id
        self.timestamp = int(time.time())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
