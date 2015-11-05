import json

data={
    "sportId": 29,
    "last": 26142386,
    "league": [
        {
            "id": 1833,
            "events": [
                {
                    "id": 383911973,
                    "starts": "2015-01-22T21:00:00Z",
                    "home": "America de Natal",
                    "away": "Barras",
                    "rotNum": "901",
                    "liveStatus": 0,
                    "status": "O",
                    "parlayRestriction": 0
                },
                {
                    "id": 383911974,
                    "starts": "2015-01-22T21:00:00Z",
                    "home": "Baraunas RN",
                    "away": "ASSU RN",
                    "rotNum": "904",
                    "liveStatus": 0,
                    "status": "O",
                    "parlayRestriction": 0
                }
            ]
        }
    ]
}

print "Sport ID is %s" % data["sportId"]

for league in data["league"]:
    print "League ID is %s " % league["id"]
    for event in league["events"]:
         print "Event id : %s starts at %s : Team 1 %s VS Team 2 %s " % (event["id"], event["starts"], event["home"], event["away"])         
    
