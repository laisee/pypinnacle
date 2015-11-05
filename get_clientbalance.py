from pinnacle_utility import Headers, BaseURL, CallAPI

url = BaseURL() + 'client/balance'
resp = CallAPI(url,'JSON', Headers())
if resp:
    print 'User Bal.', "%s$%s" % (resp["currency"],resp["availableBalance"])
    print 'Open Bets', "%s$%s" % (resp["currency"],resp["outstandingTransactions"])
else:
    print 'no data returned'
