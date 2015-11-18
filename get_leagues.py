import config
from pinnacle_utility import set_headers, call_api

def get_data():
    url = config.base_url + 'leagues?sportid=12'
    resp = call_api(url, 'XML', set_headers())
    print resp
    return resp

if __name__ == "__main__":
    get_data()
