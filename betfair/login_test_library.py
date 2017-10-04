from betfair import Betfair
from betfair.models import MarketFilter, EventTypeResult
from betfair import utils

client = Betfair('5Tkp9UblKTjP47QC', 'certs/client-2048.pem')

client.login('vime0595', 'b02460246')
import ipdb; ipdb.set_trace()

mf = MarketFilter(text_query='tennis')
locale = utils.get_kwargs(locals())

filter = mf
event_types = client.make_api_request(
            'Sports',
            'listEventTypes',
            locale,
            model=EventTypeResult,
        )

#event_types = client.list_event_types(mf)

print(len(event_types))                 # 2
print(event_types[0].event_type.name)   # 'Tennis'


client.logout()

