#!/usr/bin/env python2

"""
Python 2
"""

import urllib2
import json
import datetime
import sys
import requests


def callAping(jsonrpc_req):
    """
    make a call API-NG
    """
    try:
        req = urllib2.Request(url, jsonrpc_req, headers)
        response = urllib2.urlopen(req)
        jsonResponse = response.read()
        return jsonResponse
    except urllib2.URLError:
        print 'Oops no service available at ' + str(url)
        exit()
    except urllib2.HTTPError:
        print 'Oops not a valid operation from the service ' + str(url)
        exit()


def getEventTypes():
    """
    calling getEventTypes operation
    """
    event_type_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEventTypes", "params": {"filter":{ }}, "id": 1}'
    print 'Calling listEventTypes to get event Type ID'
    eventTypesResponse = callAping(event_type_req)
    eventTypeLoads = json.loads(eventTypesResponse)
    """
    print eventTypeLoads
    """

    try:
        eventTypeResults = eventTypeLoads['result']
        return eventTypeResults
    except:
        print 'Exception from API-NG' + str(eventTypeLoads['error'])
        exit()


def getEvent(marketId):
    """
    calling getEventTypes operation
    """
    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    event_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEvents", "params": {"filter":{"marketIds":["' + str(marketId) + '"], "marketStartTime":{"from":"' + now + '"}},"sort":"FIRST_TO_START", "maxResults":"1",}, "id": 1}'
    event_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEvents", "params": {"filter":{"marketIds":["' + str(marketId) + '"]},"sort":"FIRST_TO_START", "maxResults":"1",}, "id": 1}'
    print 'Calling listEvents to get event Type ID'
    eventResponse = callAping(event_req)
    eventLoads = json.loads(eventResponse)
    """
    print eventLoads
    """

    try:
        eventResults = eventLoads['result']
        return eventResults
    except:
        print 'Exception from API-NG' + str(eventLoads['error'])
        exit()


def getEventTypeIDForEventTypeName(eventTypesResult, requestedEventTypeName):
    """
    Extraction eventypeId for eventTypeName from evetypeResults
    """
    if(eventTypesResult is not None):
        for event in eventTypesResult:
            eventTypeName = event['eventType']['name']
            if(eventTypeName == requestedEventTypeName):
                return event['eventType']['id']
    else:
        print 'Oops there is an issue with the input'
        exit()



def getMarketCatalogue(eventTypeID, marketTypeCodes, maxResults, competitionId):
    """
    Calling marketCatalouge to get marketDetails
    """
    if (eventTypeID is not None):
        print 'Calling listMarketCatalouge Operation to get MarketID and selectionId'
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        market_catalogue_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listMarketCatalogue", "params": {"filter":{"eventTypeIds":["' + eventTypeID + '"],"competitionIds":["' + str(competitionId) + '"],"marketTypeCodes":["MATCH_ODDS"],'\
                                                                                                                                                             '"marketStartTime":{"from":"' + now + '"}},"sort":"FIRST_TO_START","maxResults":"' + str(maxResults) + '","marketProjection":["RUNNER_METADATA"]}, "id": 1}'

        """
        print  market_catalogue_req
        """
        market_catalogue_response = callAping(market_catalogue_req)
        """
        print market_catalogue_response
        """
        market_catalouge_loads = json.loads(market_catalogue_response)
        try:
            market_catalouge_results = market_catalouge_loads['result']
            return market_catalouge_results
        except:
            print  'Exception from API-NG' + str(market_catalouge_results['error'])
            exit()


def getMarketIds(marketCatalogueResults):
    marketIds = []
    if(marketCatalogueResults is not None):
        for market in marketCatalogueResults:
            marketIds.append(market['marketId'])
    return marketIds


def getSelectionIds(marketCatalogueResults):
    selectionIds = []
    for marketCatalogueResult in marketCatalogueResults:
        if(marketCatalogueResult is not None):
            runners = marketCatalogueResult['runners']
            for runner in runners:
                selectionIds.append(runner['selectionId'])
    return selectionIds


def getMarketBookBestOffers(marketId):
    print 'Calling listMarketBook to read prices for the Market with ID :' + marketId
    market_book_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listMarketBook", "params": {"marketIds":["' + marketId + '"],"priceProjection":{"priceData":["EX_BEST_OFFERS"]}}, "id": 1}'
    """
    print  market_book_req
    """
    market_book_response = callAping(market_book_req)
    """
    print market_book_response
    """
    market_book_loads = json.loads(market_book_response)
    try:
        market_book_result = market_book_loads['result']
        return market_book_result
    except:
        print  'Exception from API-NG' + str(market_book_result['error'])
        exit()


def printPriceInfo(market_book_result):
    if(market_book_result is not None):
        print 'Please find Best three available prices for the runners'
        for marketBook in market_book_result:
            runners = marketBook['runners']
            for runner in runners:
                print 'Selection id is ' + str(runner['selectionId'])
                if (runner['status'] == 'ACTIVE'):
                    print 'Available to back price :' + str(runner['ex']['availableToBack'])
                    print 'Available to lay price :' + str(runner['ex']['availableToLay'])
                else:
                    print 'This runner is not active'


def placeFailingBet(marketId, selectionId):
    if( marketId is not None and selectionId is not None):
        print 'Calling placeOrder for marketId :' + marketId + ' with selection id :' + str(selectionId)
        place_order_Req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/placeOrders", "params": {"marketId":"' + marketId + '","instructions":'\
                                                                                                                              '[{"selectionId":"' + str(
            selectionId) + '","handicap":"0","side":"BACK","orderType":"LIMIT","limitOrder":{"size":"0.01","price":"1.50","persistenceType":"LAPSE"}}],"customerRef":"test12121212121"}, "id": 1}'
        """
        print place_order_Req
        """
        place_order_Response = callAping(place_order_Req)
        place_order_load = json.loads(place_order_Response)
        try:
            place_order_result = place_order_load['result']
            print 'Place order status is ' + place_order_result['status']
            """
            print 'Place order error status is ' + place_order_result['errorCode']
            """
            print 'Reason for Place order failure is ' + place_order_result['instructionReports'][0]['errorCode']
        except:
            print  'Exception from API-NG' + str(place_order_load['error'])
        """
        print place_order_Response
        """


url = "https://api.betfair.com/exchange/betting/json-rpc/v1"

"""
headers = { 'X-Application' : 'xxxxxx', 'X-Authentication' : 'xxxxx' ,'content-type' : 'application/json' }
"""
args = len(sys.argv)

if (args < 3):
    print 'Please provide Application key and session token'
    appKey = raw_input('Enter your application key :')
    sessionToken = raw_input('Enter your session Token/SSOID :')
    print 'Thanks for the input provided'
else:
    appKey = sys.argv[1]
    sessionToken = sys.argv[2]

headers = {'X-Application': appKey, 'X-Authentication': sessionToken, 'content-type': 'application/json'}

eventTypesResult = getEventTypes()
soccerEventTypeID = getEventTypeIDForEventTypeName(eventTypesResult, 'Soccer')

print 'Eventype Id for Soccer is :' + str(soccerEventTypeID)

# get premier league id by using the listCompetition endpoint
# Use west ham vs brighton 20th of october
premierLeagueId = 10932509

interesting_market_types = [
    'OVER_UNDER_25',
    'MATCH_ODDS',
    'OVER_UNDER_35',
    'OVER_UNDER_45',
    'OVER_UNDER_15',
    'BOTH_TEAMS_TO_SCORE',
    'OVER_UNDER_05',
    'ASIAN_HANDICAP'
]

start_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

# Use market catalogue to get markets for premier league with specific betting types and dates.
import ipdb; ipdb.set_trace()

marketCatalogueResults = getMarketCatalogue(soccerEventTypeID, interesting_market_types, 2, premierLeagueId)
marketIds = getMarketIds(marketCatalogueResults)
runnerIds = getSelectionIds(marketCatalogueResults)
"""
print marketid
print runnerId
"""
events = getEvent(marketIds[0])
market_book_result = getMarketBookBestOffers(marketIds[0])
printPriceInfo(market_book_result)

#placeFailingBet(marketid, runnerId)
