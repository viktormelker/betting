from app.models.rest_classes import BetfairConnection, BetfairFilter, MyMarketCatalogue
from betfair.utils import process_result
from betfair.models import (
    CompetitionResult, Competition, EventTypeResult, EventType, MarketCatalogue,
    RunnerCatalog, Event, MarketBook, Runner
)
from betfair.constants import MarketBettingType



def print_market_data(market_id, runners):
    print(f'got data for game with marketid {market_id}')

    response = conn.crap_get_events(market_id)
    event_data = response.json()
    event = Event(**event_data[0]['event'])
    print(f'Game has event_id: {event.id}, name: {event.name} and time: {event.open_date}')

    response = conn.get_market_book(market_id)
    market_book_data = response.json()

    #import ipdb; ipdb.set_trace()

    runner_catalog_dict = {}
    all_runners = runners
    for runner in all_runners:
        runner_model = RunnerCatalog(**runner)
        runner_catalog_dict[runner_model.selection_id] = runner_model.serialize()


    runner_dict = {}
    all_runners = market_book_data[0]['runners']
    for runner in all_runners:
        runner_model = Runner(**runner)
        runner_dict[runner_model.selection_id] = runner_model.serialize()

    for key, value in runner_catalog_dict.items():
        print('Bet on %s has odds %s' % (value['runnerName'], runner_dict[key]['lastPriceTraded']))
        #print(runner_dict[key])
        #print(value)


def get_premier_league_data():

    temp_filter = BetfairFilter(textQuery='English premier league')
    response = conn.get_competitions(temp_filter)
    #print(response)
    # TODO: Use process_result
    #result = process_result(response.json(), CompetitionResult)
    premier_league = Competition(**response.json()[0]['competition'])
    print(f'The competition id for premier league is {premier_league.id}')

    temp_filter = BetfairFilter(textQuery='Soccer')
    response = conn.get_event_types(temp_filter)
    #result = process_result(response.json(), EventTypeResult)
    soccer_event_type = EventType(**response.json()[0]['eventType'])

    market_betting_type = MarketBettingType
    interesting_market_types = [
        market_betting_type.ODDS,
        market_betting_type.ASIAN_HANDICAP_SINGLE_LINE,
        market_betting_type.ASIAN_HANDICAP_DOUBLE_LINE,
    ]

    #football_filter = BetfairFilter(
    #    competitionIds=[premier_league.id],
    #    eventTypeIds=[soccer_event_type.id],
    #    marketBettingTypes=interesting_market_types
    #)

    response = conn.crap_get_market_catalogue('Man', 5)
    #print(response.json())
    market_catalog_data = response.json()
    #result = process_result(market_catalog_data, MarketCatalogue)

    for data in market_catalog_data:
        market_id = data['marketId']
        print_market_data(market_id, data['runners'])

    #market_id = market_catalog_data[0]['marketId']

    #print_market_data(market_id, market_catalog_data[0]['runners'])



def test_endpoints():
    data_filter = BetfairFilter()

    response = conn.get_events(data_filter)
    print(response)
    print(response.json())

    response = conn.get_competitions(data_filter)
    print(response)
    print(response.json())

    response = conn.get_event_types(data_filter)
    print(response)
    print(response.json())

    # TODO: marketName is mandatory?
    response = conn.get_market_catalogue(data_filter, maxResults=1)
    print(response)
    print(response.json())

    # TODO: isMarketDataDelayed is mandatory
    response = conn.get_market_book(data_filter, maxResults=1)
    print(response)
    print(response.json())



conn = BetfairConnection(
    '5Tkp9UblKTjP47QC',
    'ResOb3sbvFhbqIa5wFjY9g+JgYYaS5ebtbwWsign5Ss='
)

get_premier_league_data()