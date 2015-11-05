import json
from pinnacle_utility import Headers, BaseURL, CallAPI, LeagueLOL

def get_data():
    #url = BaseURL() + 'odds?sportId=12&leagueids=9652&oddsFormat=DECIMAL'
    url = BaseURL() + 'odds?sportId=12&leagueids='+LeagueLOL()+'&oddsFormat=DECIMAL' 
    resp = CallAPI(url,'JSON',Headers())
    if resp:
        for league in resp["leagues"]:
            print "LEAGUE : ",league["id"]
            for event in league["events"]:
                #print(event["periods"])
                period = event["periods"][0]
                if period:
                    print("Line : %s with Cutoff %s" % (period["lineId"],period["cutoff"]))
                    if 'moneyline' in period:
                        print("\t N/ODDS are Team1 %s VS Team2 %s " % (str(period["moneyline"]["home"]),str(period["moneyline"]["away"])))
                    elif 'spreads' in period:
                        print("\t H/ODDS are Team1 %s VS Team2 %s " % (str(period["spreads"][0]["home"]),str(period["spreads"][0]["away"])))
    return resp

if __name__ == "__main__":
    get_data()
