# Datetime Info
import datetime as dtm
from pytz import timezone

EST = timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S'
def currentTime(string=True):
    if string: return dtm.datetime.now(EST).strftime(fmt)
    else: return dtm.datetime.now(EST)

# SERVER CONFIGS

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

SIMULATOR_HOST = '127.0.0.1'
SIMULATOR_PORT = 5001

MARKETS_BUFFER_TIME = 2
AGENTS_BUFFER_TIME = 1
REFRESH_TIME = 1000
SIMULATE_TIME = .1

SIMULATION = True


# GAME CONFIGS

BOARD_SQUARES = 40
NUM_DICE = 2
DICE_SIDES = 6

INITIAL_CAPITAL = 2000
GO_MONEY = 50

YIELD_CURVE_MATURITIES = [1, 2, 5, 10, 20, 30, 50, 100]
YIELD_CURVE_STARTING_YIELDS =  None

NASDAQ_API_KEY = '7Co5zu-KeVjbDdv82sqs'


## SIMULATOR CONFIGS

SIMULATOR_LOG_FILE = 'simulator.log'

DEFAULT_PLAYERS = {'0': 'Dalio', 
				   '1': 'Soros'}

DEFAULT_SETTINGS = {'initial_capital': '1000', 
					'auction': '1',
					'go_around': '1'}

AGENT_SETTINGS = {'tree_depth': 10,
				  'tree_width': 2}

