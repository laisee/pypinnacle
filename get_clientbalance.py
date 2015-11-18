import config
from pinnacle_utility import set_headers, call_api

url = config.base_url + 'client/balance'
resp = call_api(url, 'JSON', set_headers())
if resp:
    print 'User Bal.', "%s$%s" % (resp["currency"], resp["availableBalance"])
    print ('Open Bets', "%s$%s" % (resp["currency"], 
           resp["outstandingTransactions"]))
else:
    print 'no data returned'
