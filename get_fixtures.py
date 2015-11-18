import config
from pinnacle_utility import set_headers, call_api, league_lol

def get_data():
    url = config.base_url + 'fixtures?sportId=12&leaguesids='+ league_lol()
    resp = call_api(url, 'JSON', set_headers())
    print resp
    return resp

if __name__ == "__main__":
    get_data()
