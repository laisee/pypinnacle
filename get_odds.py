import json

import config
from pinnacle_utility import set_headers, call_api, league_lol

def get_data():
    #url = base_url() + 'odds?sportId=12&leagueids=9652&oddsFormat=DECIMAL'
    params = 'odds?sportId=12&leagueid=%s&oddsFormat=DECIMAL' % league_lol()
    url = config.base_url + params
    resp = call_api(url, 'JSON', set_headers())
    if resp:
        for league in resp["leagues"]:
            print "\n\nLEAGUE : ", league["id"]
            for event in league["events"]:
                #print(event["periods"])
                period = event["periods"][0]
                if period:
                    print ("Line : %s with Cutoff %s" % 
                           (period["lineId"], period["cutoff"]))
                    if 'moneyline' in period:
                        print ("\t N/ODDS are Team1 %s VS Team2 %s " %
                               (period["moneyline"]["home"],
                               period["moneyline"]["away"]))
                    elif 'spreads' in period:
                        print ("\t H/ODDS are Team1 %s VS Team2 %s " %
                               (period["spreads"][0]["home"],
                               period["spreads"][0]["away"]))
    return resp

if __name__ == "__main__":
    get_data()
