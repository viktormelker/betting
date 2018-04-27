#!/usr/bin/env python

"""
Python 2
"""


import requests


### Fill these out! ###
username = ''
password = ''
application_key = ''
#######################

payload = 'username={}&password={}'.format(username, password)
headers = {'X-Application': application_key, 'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.post('https://identitysso.betfair.com/api/certlogin', data=payload, cert=('certs/client-2048.crt', 'certs/client-2048.key'), headers=headers)

if response.status_code == 200:
    response_json = response.json()
    print response_json['loginStatus']
    print response_json['sessionToken']
else:
    print "Request failed."
