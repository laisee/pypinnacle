import config
from pinnacle_utility import set_headers, call_api, league_lol

def get_data():
    SPORT_ID = '12' 
    url = config.base_url + 'fixtures?sportId='+SPORT_ID+'&leaguesids='+ league_lol()
    resp = call_api(url, 'JSON', set_headers())
    return resp

if __name__ == "__main__":
    get_data()
