"""
python 3
"""

from betfair import Betfair
from betfair.models import MarketFilter, EventTypeResult
from betfair import utils

from secrets import (
    username, password, delayed_application_key as application_key)

client = Betfair(application_key, 'certs/client-2048.pem')

try:
    client.login(username, password)

    print('session_token: ' + client.session_token)

finally:
    client.logout()

