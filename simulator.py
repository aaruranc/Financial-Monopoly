import os
import json
import time
import logging
import requests
import threading
import collections
import copy as cp
import datetime as dtm

from config import *
from helper_simulator import *
from flask import Flask, request, jsonify

# os.environ['WERKZEUG_RUN_MAIN'] = 'true'
logger = logging.getLogger('main')
logging.getLogger('werkzeug').disabled = True

AGENTS = {}
deque = collections.deque()
app = Flask(__name__)

logging.basicConfig(filename=SIMULATOR_LOG_FILE, level=logging.INFO)

@app.route("/", methods=['GET', 'POST'])
def status():

	now = dtm.datetime.now().strftime('%Y%m%d %H:%M:%S')
	
	if SIMULATION:

		# Initialize Game
		print('YEET')
		x = json.dumps(DEFAULT_PLAYERS)
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/', x, headers = {'Content-type': 'content_type_value'})
		response = r.text
		# print(r); print(response)
		if response != 'Initialized Players': return 'Unable to Initialize Players'

		# Pass Game Settings
		x = json.dumps(DEFAULT_SETTINGS)
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/play', x)
		response = r.text
		# print(r); print(response)
		if response != 'Initialized Settings':  return 'Unable to Initialize Settings'

		# Initialize Players
		AGENTS['Dalio'] = Agent('Dalio')

		# Initialize Game Loop
		data = {'state': 'not started'}
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/loop', json.dumps(data))
		response = r.text; game_data = r.json()
		# print(r); print(response); print(game_data)

		# Append Data to Deque to Start Simulating
		deque.append(['game', game_data])

		return f'Simulating up at {now}'


	else: 
		
		return f'Not simulating at {now}'


## Simulation Management
@app.route("/simulate", methods=['POST'])
def test():

	# print(deque)
	to_process = []
	while len(deque): to_process.append(deque.popleft())
	# print(to_process); print('')

	for update in to_process:

		if update[0] == 'game':


			# Get Initial Roll
			r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/roll', json.dumps(update[1]))
			response = r.text; roll_data = r.json()
			# print(r); print(response)

			# Update Player Position information based on Roll 

			# Get Potential Actions Based on Roll
			r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/action', json.dumps(roll_data))
			response = r.text; action_data = r.json()
			# print(r); print(response); print(action_data)

			# Have Player Decide Action (Currently passing back Action Dict)
			# Server Randomizes Action 
			r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/decision', json.dumps(action_data))
			response = r.text; decision_data = r.json()
			# print(r); print(response); print(decision_data)
			logger.info(currentTime() + f'-{str(decision_data)}')
        

			# Next Player Rolls
			deque.append(['game', decision_data])

	return jsonify('YEET')
	

def simulate():
	
	time.sleep(2)
	while 1:
		r = requests.post(f'http://{SIMULATOR_HOST}:{SIMULATOR_PORT}/simulate')
		time.sleep(SIMULATE_TIME)

	return

	


	# time.sleep(SIMULATE_TIME)
	# return

simulator_thread = threading.Thread(target=simulate)
simulator_thread.daemon = True



if __name__ == '__main__':

	simulator_thread.start()
	app.run(host=SIMULATOR_HOST, port=SIMULATOR_PORT, debug=True)
	simulator_thread.join()



# def update_markets():
# 	time.sleep(MARKETS_BUFFER_TIME)
	# while 1:
	# 	r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/markets')
	# 	time.sleep(REFRESH_TIME)
	# return

# markets_thread = threading.Thread(target=update_markets)
# markets_thread.daemon = True




# if __name__ == '__main__':
	
# 	markets_thread.start()
# 	app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
# 	markets_thread.join()
	


