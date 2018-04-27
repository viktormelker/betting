# betfair

## Getting premier league data
### Setup
1. Create virtualenv with python2: `virtualenv -p /usr/bin/python2 .venv2`
2. Install all requirements: `pip install -r requirements.txt`
3. Create a file in this folder called `secrets.py` on the template:
```
username = ''
password = ''
live_application_key = ''
delayed_application_key = ''
```
Fill out the needed values (at the moment all except `live_application_key`)

### Get data
1. `make login`: note the session_token!
2. `make run`: use the session_token received in step 1.