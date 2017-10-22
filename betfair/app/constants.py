
"""BetFair betting enums. See
https://api.developer.betfair.com/services/webapps/docs/display/1smk3cen4v3lu3yomq5qye0ni/Betting+Enums
"""

from enum import Enum


MARKET_PROJECTION = Enum(
    'MARKET_PROJECTION', [
        'COMPETITION',
        'MARKET_DESCRIPTION',
        'EVENT',
        'EVENT_TYPE',
        'RUNNER_METADATA',
        'RUNNER_DESCRIPTION',
        'MARKET_START_TIME',
    ]
)

PRICE_DATA = Enum(
    'PRICE_DATA', [
        'SP_AVAILABLE',
        'SP_TRADED',
        'EX_BEST_OFFERS',
        'EX_ALL_OFFERS',
        'EX_TRADED',
    ]
)

MATCH_PROJECTION = Enum(
    'MATCH_PROJECTION', [
        'NO_ROLLUP',
        'ROLLED_UP_BY_PRICE',
        'ROLLED_UP_BY_AVG_PRICE',
    ]
)

OREDER_PROJECTION = Enum(
    'OREDER_PROJECTION', [
        'ALL',
        'EXECUTABLE',
        'EXECUTION_COMPLETE',
    ]
)

MARKET_STATUS = Enum(
    'MARKET_STATUS', [
        'INACTIVE',
        'OPEN',
        'SUSPENDED',
        'CLOSED',
    ]
)

RUNNER_STATUS = Enum(
    'RUNNER_STATUS', [
        'ACTIVE',
        'WINNER',
        'LOSER',
        'REMOVED_VACANT',
        'REMOVED',
        'HIDDEN',
    ]
)

TIME_GRANULARITY = Enum(
    'TIME_GRANULARITY', [
        'DAYS',
        'HOURS',
        'MINUTES',
    ]
)

SIDE = Enum(
    'SIDE', [
        'BACK',
        'LAY',
    ]
)

ORDER_STATUS = Enum(
    'ORDER_STATUS', [
        'EXECUTION_COMPLETE',
        'EXECUTABLE',
    ]
)

ORDER_BY = Enum(
    'ORDER_BY', [
        'BY_BET',
        'BY_MARKET',
        'BY_MATCH_TIME',
        'BY_PLACE_TIME',
        'BY_SETTLED_TIME',
        'BY_VOID_TIME',
    ]
)

SORT_DIR = Enum(
    'SORT_DIR', [
        'EARLIEST_TO_LATEST',
        'LATEST_TO_EARLIEST',
    ]
)

ORDER_TYPE = Enum(
    'ORDER_TYPE', [
        'LIMIT',
        'LIMIT_ON_CLOSE',
        'MARKET_ON_CLOSE',
    ]
)

MARKET_SORT = Enum(
    'MARKET_SORT', [
        'MINIMUM_TRADED',
        'MAXIMUM_TRADED',
        'MINIMUM_AVAILABLE',
        'MAXIMUM_AVAILABLE',
        'FIRST_TO_START',
        'LAST_TO_START',
    ]
)

MARKET_BETTING_TYPE = Enum(
    'MARKET_BETTING_TYPE', [
        'ODDS',
        'LINE',
        'RANGE',
        'ASIAN_HANDICAP_DOUBLE_LINE',
        'ASIAN_HANDICAP_SINGLE_LINE',
        'FIXED_ODDS',
    ]
)

EXECUTION_REPORT_STATUS = Enum(
    'EXECUTION_REPORT_STATUS', [
        'SUCCESS',
        'FAILURE',
        'PROCESSED_WITH_ERRORS',
        'TIMEOUT',
    ]
)

EXECUTION_REPORT_ERROR_CODE = Enum(
    'EXECUTION_REPORT_ERROR_CODE', [
        'ERROR_IN_MATCHER',
        'PROCESSED_WITH_ERRORS',
        'BET_ACTION_ERROR',
        'INVALID_ACCOUNT_STATE',
        'INVALID_WALLET_STATUS',
        'INSUFFICIENT_FUNDS',
        'LOSS_LIMIT_EXCEEDED',
        'MARKET_SUSPENDED',
        'MARKET_NOT_OPEN_FOR_BETTING',
        'DUPLICATE_TRANSACTION',
        'INVALID_ORDER',
        'INVALID_MARKET_ID',
        'PERMISSION_DENIED',
        'DUPLICATE_BETIDS',
        'NO_ACTION_REQUIRED',
        'SERVICE_UNAVAILABLE',
        'REJECTED_BY_REGULATOR',
    ]
)

PERSISTANCE_TYPE = Enum(
    'PERSISTANCE_TYPE', [
        'LAPSE',
        'PERSIST',
        'MARKET_ON_CLOSE',
    ]
)

INSTRUCTION_REPORT_STATUS = Enum(
    'INSTRUCTION_REPORT_STATUS', [
        'SUCCESS',
        'FAILURE',
        'TIMEOUT',
    ]
)

INSTRUCTION_REPORT_ERROR_CODE = Enum(
    'INSTRUCTION_REPORT_ERROR_CODE', [
        'INVALID_BET_SIZE',
        'INVALID_RUNNER',
        'BET_TAKEN_OR_LAPSED',
        'BET_IN_PROGRESS',
        'RUNNER_REMOVED',
        'MARKET_NOT_OPEN_FOR_BETTING',
        'LOSS_LIMIT_EXCEEDED',
        'MARKET_NOT_OPEN_FOR_BSP_BETTING',
        'INVALID_PRICE_EDIT',
        'INVALID_ODDS',
        'INSUFFICIENT_FUNDS',
        'INVALID_PERSISTENCE_TYPE',
        'ERROR_IN_MATCHER',
        'INVALID_BACK_LAY_COMBINATION',
        'ERROR_IN_ORDER',
        'INVALID_BID_TYPE',
        'INVALID_BET_ID',
        'CANCELLED_NOT_PLACED',
        'RELATED_ACTION_FAILED',
        'NO_ACTION_REQUIRED',
    ]
)

ROLLUP_MODEL = Enum(
    'ROLLUP_MODEL', [
        'STAKE',
        'PAYOUT',
        'MANAGED_LIABILITY',
        'NONE',
    ]
)

GROUP_BY = Enum(
    'GROUP_BY', [
        'EVENT_TYPE',
        'EVENT',
        'MARKET',
        'SIDE',
        'BET',
    ]
)

BET_STATUS = Enum(
    'BET_STATUS', [
        'SETTLED',
        'VOIDED',
        'LAPSED',
        'CANCELLED',
    ]
)

EXCHANGE = Enum(
    'EXCHANGE', [
        'AUS',
        'UK',
    ]
)

ENDPOINT = Enum(
    'ENDPOINT', [
        'Betting',
        'Account',
    ]
)

WALLET = Enum(
    'WALLET', [
        'UK',
        'AUSTRALIAN',
    ]
)

INCLUDE_ITEM = Enum(
    'INCLUDE_ITEM', [
        'ALL',
        'DEPOSITS_WITHDRAWALS',
        'EXCHANGE',
        'POKER_ROOM',
    ]
)

ITEM_CLASS = Enum(
    'ITEM_CLASS', [
        'UNKNOWN',
    ]
)