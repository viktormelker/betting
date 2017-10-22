from app.models.rest_classes import BetfairConnection, BetfairFilter
from betfair.utils import process_result
from betfair.models import (
    CompetitionResult, Competition, EventTypeResult, EventType
)
from betfair.constants import MarketBettingType


def get_premier_league_data():
    import ipdb; ipdb.set_trace()

    temp_filter = BetfairFilter(textQuery='English premier league')
    response = conn.get_competitions(temp_filter)
    #print(response)
    # TODO: Use process_result
    #result = process_result(response.json(), CompetitionResult)
    premier_league = Competition(**response.json()[0]['competition'])
    print(f'The competition id for premier league is {premier_league.id}')

    temp_filter = BetfairFilter(textQuery='Soccer')
    response = conn.get_event_types(temp_filter)
    print(response)
    print(response.json())
    #result = process_result(response.json(), EventTypeResult)
    soccer_event_type = EventType(**response.json()[0]['eventType'])

    market_betting_type = MarketBettingType
    interesting_market_types = [
        market_betting_type.ODDS,
        market_betting_type.ASIAN_HANDICAP_SINGLE_LINE,
        market_betting_type.ASIAN_HANDICAP_DOUBLE_LINE,
    ]

    football_filter = BetfairFilter(
        competitionIds=[premier_league.id],
        eventTypeIds=[soccer_event_type.id],
        marketBettingTypes=interesting_market_types
    )

    response = conn.get_market_catalogue(football_filter, maxResults=10)
    print(response)
    print(response.json())


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

    import ipdb; ipdb.set_trace()
    # TODO: marketName is mandatory!
    response = conn.get_market_catalogue(data_filter, maxResults=1)
    print(response)
    print(response.json())

    # TODO: isMarketDataDelayed is mandatory
    response = conn.get_market_book(data_filter, maxResults=1)
    print(response)
    print(response.json())



conn = BetfairConnection(
    '5Tkp9UblKTjP47QC',
    '0mB8ozzrNR4445gzaRVoh7LtdIzLijOeNRv15Kl1L9k='
)

get_premier_league_data()