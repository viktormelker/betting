from app.models.rest_classes import BetfairConnection, BetfairFilter

import ipdb; ipdb.set_trace()
conn = BetfairConnection('5Tkp9UblKTjP47QC', '0mB8ozzrNR4445gzaRVoh7LtdIzLijOeNRv15Kl1L9k=')

data_filter = BetfairFilter()

response = conn.get_events(data_filter)
print(response)

response = conn.get_competitions(data_filter)
print(response)

response = conn.get_event_types(data_filter)
print(response)

response = conn.get_market_catalogue(data_filter, maxResults=1)
print(response)

response = conn.get_market_book(data_filter)
print(response)
