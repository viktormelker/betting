import requests
import json
#import re
from betfair.models import MarketFilter
from betfair.meta.utils import serialize_dict


class BetfairFilter(MarketFilter):

    def to_json(self):
        # TODO: Adapt to handle list objects
        raw_json = serialize_dict(self)
        active_filters = []
        for key in raw_json:
            if raw_json[key] is not None:
                text = f'"{key}": "{raw_json[key]}"'
                #text = re.sub(', ''', text)
                active_filters.append(text)
        final_json = ', '.join(active_filters)
        return '"filter":{%s}' % final_json


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

    def get_market_book(self, data_filter: BetfairFilter, maxResults: int):
        data = '{%s, "maxResults":%i}' % (data_filter.to_json(), maxResults)
        return self.make_request('listMarketBook/', data)

    def make_request(self, spec_endpoint, data):
        url = self.endpoint + spec_endpoint
        return requests.post(url, data=data, headers=self.headers)
