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

		
		player_d = {'0': 'Dalio', 
					'1': 'Soros'}



		print('YEEEET')
		x = json.dumps(player_d)

		print(x)

		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/initialize', x)
		print(r)
		# data = r.text()
 

		return f'Simulating up at {now}'


	else: 
		
		return f'Not simulating at {now}'


@app.route("/players", methods=['GET', 'POST'])
def players():

	player_d = {'0': 'Dalio', 
				'1': 'Soros'}

	return jsonify(player_d)



@app.route("/settings", methods=['GET', 'POST'])
def settings():

	settings_d = {'initial_capital': '1000', 
				  'auction': '1',
				  'go_around': '1'}

	return jsonify(settings_d)





	# r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/initialize', jsonify(player_d))
	# print(r.text)


	


	# return 'yeet'





if __name__ == '__main__':
	app.run(host=SIMULATOR_HOST, port=SIMULATOR_PORT, debug=True)