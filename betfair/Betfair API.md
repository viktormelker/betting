# Betfair API

## General information
* Costs 299£ for a live key to do automated betting.
* Has example implementations in [python](https://github.com/jmcarp/betfair.py)
* Some [navigation guide](http://docs.developer.betfair.com/docs/display/1smk3cen4v3lu3yomq5qye0ni/Understanding+Market+Navigation)

## Getting development keys
Follow guide: https://developer.betfair.com/get-started/#exchange-api
Application Name chosen in api demo: viktorgetrich

## Generate public key
1. Follow guide on `http://docs.developer.betfair.com/docs/display/1smk3cen4v3lu3yomq5qye0ni/Non-Interactive+%28bot%29+login`

## Logging in
* It seems to be possible to be possible to use single sign on and be authenticated that way. Follow [guide](Generate-public-key).
* Otherwise the delay key and the session token can be used in the headers if user is already signed in on the betfair normal webpage.

## Several APIs
1. Betting API  - Contains navigation, odds retrieval and bet placement operations.
2. Accounts API - Contains account related operations such as the ability to retrieve your available account balance as well as Vendor Services operations that are available to licensed Software Vendors
3. Heartbeat API - allows you to automatically cancel unmatched bets in the event of your API client/s losing connectivity.
4.Race Status API - allows you to establish the status of a horse race or greyhound market both prior to and after the start of the race. 
5.Exchange Stream API - allows you to subscribe to market changes (both price and definitions) and orders.


## Operations (Betting api)
* listEventTypes - List different sports etc to bet on.
* listCompetitions - Champions League, US open etc
* listTimeRanges - Date intervals whith bets 
* listEvents - specific games. Some team names are abbreviations! Has start date and time
* listMarketTypes - Type of bets
* listCountries - Countries
* listVenues - Venue
* listMarketCatalogue - Get hold of the marketId of specific events
* listMarketBook - Probably returns price data etc. Call using market id returned by listMarketCatalogue
* listRunnerBook - ???
* placeOrders - 
* updateOrders - 
* replaceOrders - 
* listCurrentOrders - 
* listClearedOrders -
* listMarketProfitAndLoss - 

### Possible approach:
1. Use listMarketType to see which types of bets are available.
2. Select the bet types that can be used together
3. Take one set of bets that go together. Use them in the marketfilter
4. Use ListEvents to find games to play on
5. Use listMarketCatalogue with the specific eventIds to get marketIds. Set maxResults to be higher than 1!
6. Use listMarketBook to get the odds of all marketIds that were received
7. Check all odds for every bet type for a specific game (what endpoint???), see if there is an arbitrage possibility.
8. Do this by combining with competitors of betfair also.

## Operations (Accounts API)
* createDeveloperAppKeys
* getDeveloperAppKeys

### Questions
* How do we get a specific bet/odds for a game? listEvents only say the game, not the bet type or the odds!

## Testing the API
1: Log in to Betfair
2: Go to https://developer.betfair.com/exchange-api/betting-api-demo/
3: Session Token should be filled in.
4: Enter App key using the Delay key above
5: Select API operation, press execute

## General requirements on API
The following requirements must be fullfilled in order for our betting strategy to work:
1. It must be possible to see games with a timestamp (to match games)
2. It must be possible to see different bets on specific games and their respective odds.
3. It must be possible to place bets
4. It must be possible to see account balance, (placed odds and when they are due).
5. Login

