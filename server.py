import json
import time
import requests
import threading

from config import *
from helper_server import *
from flask import Flask, request, render_template, jsonify


np.random.seed(6)

game = Game()
markets = Markets()
settings = Settings() 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def initialize():
	
	print('YERRRR')

	if request.method == 'GET':
		return render_template('main.html')

	elif request.method == 'POST':
		
		data = json.loads(request.data)
		game.num_players = len(data)

		for key in data:
			player_dict[int(key)] = Player(data[key])

	# Server Based Simulation
	if SIMULATION:
		return 'Initialized Players'
	
	# Web Based Play
	else:
		return render_template('settings.html')



@app.route("/play", methods=['POST'])
def play():

	# Process Settings and Update Player Dict and Game Object
	# Cleaner way to update? (re: auction/go_around)

	data = json.loads(request.data)
	for key in data:
		settings_dict[key] = data[key]
		if key == 'initial_capital':
			for pl in player_dict:
				player_dict[pl].capital = int(data[key])
		elif key == 'auction':
			settings.auction = data[key]
		elif key == 'go_around':
			settings.go_around = data[key]

	# Server Based Simulation
	if SIMULATION:
		return 'Initialized Settings'
	
	# Web Based Play
	else:
		return render_template('play.html')


# Redundant Design, could be structured as a better API call
@app.route("/loop", methods=['POST'])
def loop():

	# This endpoint is probably redundant since it's only hit once
	# Better design is to handle in /roll with intialization if block

	d = {}
	data = json.loads(request.data)
	# print('loop', data)

	if data['state'] == 'not started': curr_player = 0
	player = player_dict[curr_player]
	d['current_player'] = curr_player
	d['player_name'] = player.name
	d['position'] = player.position
	d['capital'] = player.capital
	
	return jsonify(d)


@app.route("/roll", methods=['POST'])
def roll():

	data = json.loads(request.data)
	print('roll', data)

	player = player_dict[data['current_player']]
	roll_num = np.random.randint(1, NUM_DICE * DICE_SIDES)

	data['roll_num'] =  roll_num

	new_position = data['position'] + data['roll_num']
	if new_position >= BOARD_SQUARES:
		new_position = new_position % BOARD_SQUARES

		# Add Go Money for going around board
		player.capital += GO_MONEY

	# Setting internal player position before user notification
	data['position'] = player.position = new_position

	return jsonify(data)


@app.route("/action", methods=['POST'])
def action():

	data = json.loads(request.data)
	print('action', data)

	player_options = game.player_actions(data)


	return jsonify(player_options)

	# Map current Game State and Player state to potential actions
	# Leaving blank for now 

	# next_player = (data['current_player'] + 1 ) % game.num_players
	# player = player_dict[next_player]

	# d = {}
	# d['current_player'] = next_player
	# d['player_name'] = player.name
	# d['position'] = player.position
	# d['capital'] = player.capital

	return jsonify(d)	


@app.route("/decision", methods=['POST'])
def decision():

	data = json.loads(request.data)
	print('decision', data)

	# Current Implementation Randomizes Buying
	outcome = game.process_decision(data)

	print('outcome', data)

	return jsonify(outcome)



@app.route("/state", methods=['GET', 'POST'])
def state():

	if request.method == 'GET':
		return render_template('state.html')

	elif request.method == 'POST':

		dd = {}
		for pl in player_dict:
			dd[pl] = vars(player_dict[pl])

			# Can't Jsonify Custom Objects, Handle Processing Better
			if 'property' in dd[pl]:
				del dd[pl]['property']

		d = {'players': dd}

		return jsonify(d)




## Markets Management
@app.route("/markets", methods=['POST'])
def test():
	return jsonify('YEET')


def update_markets():
	time.sleep(MARKETS_BUFFER_TIME)
	while 1:
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/markets')
		time.sleep(REFRESH_TIME)
	return

markets_thread = threading.Thread(target=update_markets)
markets_thread.daemon = True




if __name__ == '__main__':
	
	markets_thread.start()
	app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
	markets_thread.join()
	