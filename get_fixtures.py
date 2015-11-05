from pinnacle_utility import Headers, BaseURL, CallAPI, LeagueLOL

def get_data():
    url = BaseURL() + 'fixtures?sportId=12&leaguesids='+LeagueLOL()
    resp = CallAPI(url,'JSON',Headers())
    print resp
    return resp

if __name__ == "__main__":
    get_data()
