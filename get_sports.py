import config
from pinnacle_utility import set_headers, call_api

def get_data():
    url = config.base_url + 'sports'
    resp = call_api(url,'XML', set_headers())
    return resp

if __name__ == "__main__":
    get_data()
