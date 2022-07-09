import json
import time
import requests
import threading

from config import *
from server_helper import *
from flask import Flask, request, render_template, jsonify


np.random.seed(6)

game = Game()
markets = Markets()
settings = Settings() 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def initialize():

	if request.method == 'GET':
		# print('yeet')
		return render_template('main.html')

	elif request.method == 'POST':
		
		keys = list(request.form.keys())
		# print(keys)

		for key in keys:
			player_dict[int(key)] = Player(request.form[key])

		game.num_players = len(keys)

		return render_template('settings.html')


@app.route("/play", methods=['POST'])
def play():

	# Process Settings and Update Player Dict and Game Object
	# Cleaner way to update? (re: auction/go_around)
	# print(request.form)
	for key in list(request.form.keys()):
		settings_dict[key] = request.form[key]
		if key == 'initial_capital':
			for pl in player_dict:
				player_dict[pl].capital = int(request.form[key])
		elif key == 'auction':
			settings.auction = request.form[key]
		elif key == 'go_around':
			settings.go_around = request.form[key]

	return render_template('play.html')


@app.route("/loop", methods=['POST'])
def loop():

	# This endpoint is probably redundant since it's only hit once
	# Better design is to handle in /roll with intialization if block

	data = request.get_json()
	# print('loop', data)

	d = {}
	if data['state'] == 'not started': curr_player = 0

	player = player_dict[curr_player]
	d['current_player'] = curr_player
	d['player_name'] = player.name
	d['position'] = player.position
	d['capital'] = player.capital


	return jsonify(d)


@app.route("/roll", methods=['POST'])
def roll():

	data = request.get_json()
	print('roll', data)

	player = player_dict[data['current_player']]
	roll_num = np.random.randint(1, NUM_DICE * DICE_SIDES)

	data['roll_num'] =  roll_num

	new_position = data['position'] + data['roll_num']
	if new_position >= BOARD_SQUARES:
		new_position = new_position % BOARD_SQUARES

	# Setting internal player position before user notification
	data['position'] = player.position = new_position

	return jsonify(data)


@app.route("/action", methods=['POST'])
def action():

	data = request.get_json()
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

	data = request.get_json()
	print('decision', data)

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


def refresh_markets():
	time.sleep(BUFFER_TIME)
	while 1:
		r = requests.post(f'http://{SERVER_HOST}:{SERVER_PORT}/markets')
		time.sleep(REFRESH_TIME)
	return

markets_thread = threading.Thread(target=refresh_markets)
markets_thread.daemon = True




if __name__ == '__main__':
	
	markets_thread.start()
	app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
	markets_thread.join()
	