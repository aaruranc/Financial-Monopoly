import json
import requests
import datetime as dtm

from config import *
from simulator_helper import *
from flask import Flask, request, jsonify




app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def status():

	now = dtm.datetime.now().strftime('%Y%m%d %H:%M:%S')
	
	if SIMULATION:

		print('YEEEET')
		x = json.dumps(DEFAULT_PLAYERS)
		print(x, type(x))
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/', x)
		response = r.text
		print(response)

		if response != 'Initialized Players': 
			return 'Unable to Initialize Players'

		x = json.dumps(DEFAULT_SETTINGS)
		print(x, type(x))
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/play', x)
		response = r.text
		print(response)

		if response != 'Initialized Settings': 
			return 'Unable to Initialize Settings'

		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/loop', json.dumps({}))
		response = r.text
		print(response)


		return f'Simulating up at {now}'


	else: 
		
		return f'Not simulating at {now}'


if __name__ == '__main__':
	app.run(host=SIMULATOR_HOST, port=SIMULATOR_PORT, debug=True)