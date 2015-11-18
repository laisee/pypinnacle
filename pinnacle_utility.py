import base64, json, sys, time, traceback

import requests

import config
from pinnacle_models import *

def league_lol():
    # return ("5474,4586, 191533,5024,5467,5072,48012,9440,4680, 4979, 191468,
    #          10269, 9754, 10392, 187724, 5625, 7245, 10422, 9457, 10093, 
    #          9667, 6262, 192095")
    return "149079"
    
def get_timestamp():
    return time.mktime(time.gmtime())

def add_update_odds(data):
    match_count = 0
    odds_count = 0
    match_query = "select * from Matches where id = %s" % data.event_id
    odds_query  = "select * from Odds where event_id = %s" % data.event_id
    for match in Matches.raw(match_query):
        match_count += 1
    if match_count == 0:
       print 'No Match record found for ID == ',data.id
       return
    for odds in Matches.raw(odds_query):
        odds_count += 1
    if odds_count == 0:
        Odds.create(
                    event=data.event_id, team1_odds=data.team1_odds,
                    team2_odds = data.team2_odds, timestamp=get_timestamp())
        print "Adding Odds with Event ID %s" % data.event_id
        odds = Odds.get(event=data.event_id)
        print "Added Odds with ID %s and Event ID %s" % (odds.id, odds.event)
    else:
        odds = Odds.select(Odds.event==data.event_id).limit(1)[0]
        print ("Found Odds with Event ID %s  ts: %s" % (data.event_id, 
               odds.timestamp))
        #if (odds.team1_odds != data.team1_odds or
        #    odds.team2_odds != data.team2_odds):
        #    odds.team1_odds = data.team1_odds
        #    odds.team2_odds = data.team2_odds
        #    odds.event = data.event_id
        #    odds.timestamp = get_timestamp()
        #    odds.save()
        print "Updated Odds with Event ID %s" % data.event_id

def add_update_record(entity,data):
    count = 0
    query = "select * from %s where id = %s" % (entity, (data.id))
    try:
        database.connect()
    except OperationalError as e:
        print "Exception in database connection:", e
        exit(1)
    if entity.upper() == 'SPORT':
        for sport in Sport.raw(query):
            count += 1
        if count == 0:
            print 'No ', entity,' record found for ID == ', data.id
            Sport.create(
                         id=data.id, name=data.name, 
                         timestamp=get_timestamp())
            sport = Sport.get(Sport.id==data.id)
            #print sport.id, sport.name, sport.timestamp
        else:
            sport = Sport.get(Sport.id==data.id)
            print "Found Sport with ID %s ts %s"  % (data.id, sport.timestamp)
            sport.name = data.name
            sport.timestamp = get_timestamp()
            sport.save()
    elif entity.upper() == 'LEAGUE':
        for league in League.raw(query):
            count += 1
        if count == 0:
            print 'No ',entity,' record found for ID == ',data.id
            League.create(
                          id=data.id, name=data.name, hometeam=data.hometeam,
                          timestamp=get_timestamp())
            league = League.get(League.id==data.id)
            print league.id, league.name, league.timestamp
        else:
            league = League.get(League.id==data.id)
            print "Found League with ID",str(data.id), ' ts ', league.timestamp
            league.name = data.name
            league.timestamp = get_timestamp()
            league.save()
    elif entity.upper() == 'MATCHES':
        for event in Matches.raw(query):
            count += 1
        if count == 0:
            print 'No ',entity,' record found for ID == ',data.id
            Matches.create(
                id=data.id, start=data.start, team1=data.team1,
                team2=data.team2, timestamp=get_timestamp())
            match = Matches.get(Matches.id==data.id)
            print (match.id, match.start, match.team1, match.team2, 
                  match.timestamp)
        else:
            match = Matches.get(Matches.id==data.id)
            print ('Found ',entity,' with ID',str(data.id), ' ts ',
                   match.timestamp)
            match.start = data.start,
            match.team1 = data.team1,
            match.team2 = data.team2,
            match.timestamp = get_timestamp()
            match.save()
    else:
        print "ERROR ; invalid entity type passed to add_update_record(): \
               %s " % entity


def set_headers():
    credentials = encoded_auth(config.username, config.pswd)
    auth_header = { 'Authorization': 'Basic ' + credentials }
    return auth_header

def encoded_auth(username, pswd):
   b64creds = base64.b64encode(":".join([username, pswd]))
   return b64creds

def call_api(url, format, hdrs=None, params=None):
    print "URL ", url 
    if params:
       url = "%s%s" % (url, params)
    try:
        response = requests.get(url, headers=hdrs)
        response.raise_for_status()
        if format == 'XML':
            return response.text
        else:
            print response
            return response.json()
    except Exception as e:
        print "Exception in API request %s : %s " % (url, e)
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60
