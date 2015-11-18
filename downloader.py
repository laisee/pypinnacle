import isodate
import time
from xml.dom import minidom

import config
import models.sport as SP 
import models.league as LG 
import models.match as MT 
import models.odds as OD 
from get_sports import get_data as get_sports 
from get_leagues import get_data as get_leagues 
from get_fixtures import get_data as get_fixtures 
from get_odds import get_data as get_odds 
from pinnacle_utility import add_update_record, add_update_odds


def reload_odds():
    data = get_odds()
    #if data:
    #  for league in data["leagues"]:
    #      for event in league["events"]:
    #          odds = OD.Odds(
    #                         event["periods"][0]["moneyline"]["home"],
    #                         event["periods"][0]["moneyline"]["away"],
    #                         event["id"])
    #          print ('Event '+ str(event["id"]) + ' has MAX ' + 
    #                 str(event["periods"][0]["maxMoneyline"]) + 
    #                 ' ODDS are Team1 '+
    #                 str(event["periods"][0]["moneyline"]["home"]) + 
    #                 ' VS Team2 ' +
    #                 str(event["periods"][0]["moneyline"]["away"]))
    #          print odds.event_id, odds.team1_odds, odds.team2_odds
    #          add_update_odds(odds)
    if data:
       for league in data["leagues"]:
           print "LEAGUE : ",league["id"]
           for event in league["events"]:
               #print(event["periods"])
               period = event["periods"][0]
               if period:
                   print("Line : %s with Cutoff %s" % (period["lineId"],
                         period["cutoff"]))
                   if 'moneyline' in period:
                       #print("\t N/ODDS are Team1 %s VS Team2 %s " 
                       #      % period["moneyline"]["home"],
                       #      period["moneyline"]["away"]))
                       odds = OD.Odds(
                                      event["periods"][0]["moneyline"]["home"],
                                      event["periods"][0]["moneyline"]["away"],
                                      event["id"])
                   elif 'spreads' in period:
                       odds = OD.Odds(
                                      period["spreads"][0]["home"],
                                      period["spreads"][0]["away"],
                                      event["id"])
                       #print("\t H/ODDS are Team1 %s VS Team2 %s " % 
                       #      (period["spreads"][0]["home"],
                       #      period["spreads"][0]["away"]))
               print odds.event_id, odds.team1_odds, odds.team2_odds
               add_update_odds(odds)

def reload_matches():
    data = get_fixtures()
    if data:
        for league in data["league"]:
            for event in league["events"]:
                print ("Match id : %s starts at %s : Team 1 %s VS! Team 2 %s "
                       % (event["id"], event["starts"], event["home"], 
                        event["away"]))
                match = MT.Match(
                                 event["id"],
                                 isodate.parse_datetime(event["starts"]),
                                 event["home"],event["away"],league["id"])
                add_update_record('Matches', match)

def reload_leagues():
    data = get_leagues()
    if data:
         xmldoc = minidom.parseString(data)
         leagues = xmldoc.getElementsByTagName('league')
         for child in leagues:
             #print(' League['+child.attributes["id"].value+'] - ' +
             #      child.firstChild.nodeValue)
             lg = LG.League(
                            child.attributes["id"].value, 
                            child.firstChild.nodeValue, 
                            child.attributes["homeTeamType"].value)
             #print ('League ['+ str(lg.id) +'] - ' + lg.name + 
             #       ' downloaded @ ' + str(lg.timestamp))
             add_update_record('League', lg)

def reload_sports():
    data = get_sports()
    if data:
         xmldoc = minidom.parseString(data)
         sports = xmldoc.getElementsByTagName('sport')
         for child in sports:
             #print(' Sport['+child.attributes["id"].value+'] - '+
             #      child.firstChild.nodeValue )
             sp = SP.Sport(
                           child.attributes["id"].value,
                           child.firstChild.nodeValue)
             #print ('Sport ['+ str(sp.id) +'] - ' + sp.name + 
             #       ' downloaded @ ' + str(sp.timestamp))
             add_update_record('Sport', sp)

def reload(name='ALL'):
    if name == 'SPORTS' or name == 'ALL':
        print "\nUpdating SPORTS data\n"
        reload_sports()
    if name == 'LEAGUES' or name == 'ALL':
        print "\nUpdating LEAGUE data\n"
        reload_leagues()
    if name == 'MATCHES' or name == 'ALL':
        print "\nUpdating MATCH data\n"
        reload_matches()
    if name == 'ODDS' or name == 'ALL':
        print "\nUpdating ODDS data\n"
        reload_odds()

if __name__ == "__main__":
    print "\n\nStarting data downloader ...\n"
    run = None # is this needed?
    while True:
        print "\nNew iteration for updating source data ...\n"
        reload()
        print "\niteration completed for updating source data ...\n"
        print "\nAbout to sleep for %s secs" % config.SLEEPTIME
        time.sleep(config.SLEEPTIME)
