from pinnacle_utility import Headers, BaseURL, CallAPI

def get_data():
    url = BaseURL() + 'leagues?sportid=12'
    resp = CallAPI(url,'XML', Headers())
    print resp
    return resp

if __name__ == "__main__":
    get_data()
