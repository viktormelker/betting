"""
python 3
"""

from betfair import Betfair
from betfair.models import MarketFilter, EventTypeResult
from betfair import utils


### Fill these out! ###
username = ''
password = ''
application_key = ''
#######################

client = Betfair(application_key, 'certs/client-2048.pem')

try:
    client.login(username, password)

    print(client.session_token)

finally:
    client.logout()

