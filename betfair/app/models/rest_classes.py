import requests
import json
import re
from betfair.models import MarketFilter, RunnerCatalog
from betfair.meta.utils import serialize_dict

from schematics.types import FloatType
from schematics.types import StringType

from schematics.types.compound import ListType
from schematics.types.compound import ModelType

from betfair.meta.models import BetfairModel


class BetfairFilter(MarketFilter):

    def to_json(self):
        # TODO: Adapt to handle list objects
        raw_json = serialize_dict(self)
        raw_json = self.serialize()
        active_filters = []

        for key in raw_json:
            if raw_json[key] is not None:
                text = f'"{key}": "{str(raw_json[key])}"'
                #text2 = '"%s": "%s"' % (key, raw_json[key])
                #text = f'"{key}": "{raw_json[key]}"'
                #text = text.replace("\'", "")
                #temp = {key: raw_json[key]}
                active_filters.append(text)
        final_json = ', '.join(active_filters)
        return '"filter":{%s}' % final_json


class MyMarketCatalogue(BetfairModel):
    market_id = StringType()
    market_name = StringType()
    total_matched = FloatType()
    runners = ListType(ModelType(RunnerCatalog))


class BetfairConnection:
    def __init__(self, app_key: str, session_token: str):
        self.endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"
        self.headers = {
            'X-Application': app_key,
            'X-Authentication': session_token,
            'content-type': 'application/json'
        }

    def get_events(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listEvents/', data)

    def get_competitions(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listCompetitions/', data)

    def get_event_types(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listEventTypes/', data)

    def get_market_catalogue(self, data_filter: BetfairFilter, maxResults: int):
        data = '{%s, "maxResults":%i}' % (data_filter.to_json(), maxResults)
        return self.make_request('listMarketCatalogue/', data)


    def make_request(self, spec_endpoint, data):
        url = self.endpoint + spec_endpoint
        return requests.post(url, data=data, headers=self.headers)

    def crap_get_market_catalogue(self, text, max_results):
        data = '{"filter":{"textQuery": "%s", "eventTypeIds": [1], "competitionIds": [10932509], "marketTypeCodes": ["MATCH_ODDS"], "marketBettingTypes": ["ODDS", "ASIAN_HANDICAP_SINGLE_LINE", "ASIAN_HANDICAP_DOUBLE_LINE"],"marketStartTime":{"from":"2017-10-23T20:14:20Z"}},"sort":"FIRST_TO_START", "maxResults":%s, "marketProjection":["RUNNER_METADATA"]}' % (text, max_results)
        return self.make_request('listMarketCatalogue/', data)

    def crap_get_events(self, market_id):
        data = '{"filter":{"marketIds": ["%s"]}}' % market_id
        return self.make_request('listEvents/', data)

    def get_market_book(self, market_id):
        #data = '{"marketIds": ["%s"], priceProjection: {priceData: ["EX_BEST_OFFERS"]}}' % market_id
        data = '{"marketIds": ["%s"]}' % market_id
        return self.make_request('listMarketBook/', data)