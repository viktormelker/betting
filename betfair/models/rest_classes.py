import json
import datetime
import requests


class BetfairFilter:

    def to_json(self):
        return '"filter":{ }'


class BetfairConnection:
    def __init__(self, app_key: str, session_token: str):
        self.endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"
        self.headers = {'X-Application': app_key, 'X-Authentication': session_token, 'content-type': 'application/json'}

    def get_events(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listEvents/', data)

    def get_competitions(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listCompetitions/', data)

    def get_event_types(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listEventTypes/', data)

    def get_market_catalogue(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listMarketCatalogue/', data)

    def get_market_book(self, data_filter: BetfairFilter):
        data = '{%s}' % data_filter.to_json()
        return self.make_request('listMarketBook/', data)

    def make_request(self, spec_endpoint, data):
        url = self.endpoint + spec_endpoint
        return requests.post(url, data=data, headers=self.headers)




import ipdb; ipdb.set_trace()
conn = BetfairConnection('5Tkp9UblKTjP47QC', 'VKH/oMx+GnSiz3iPLxBV70mo39nJ959fVE7nDDbHwkg=')
data_filter = BetfairFilter()

response = conn.get_events(data_filter)
print(response)

response = conn.get_competitions(data_filter)
print(response)

response = conn.get_event_types(data_filter)
print(response)

