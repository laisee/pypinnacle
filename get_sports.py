from pinnacle_utility import Headers, BaseURL, CallAPI

def get_data():
    url = BaseURL() + 'sports'
    resp = CallAPI(url,'XML', Headers())
    return resp

if __name__ == "__main__":
    get_data()
