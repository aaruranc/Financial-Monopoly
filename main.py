import json
import numpy as np

from config import *
from helper import *
from flask import Flask, request, render_template, jsonify


np.random.seed(6)

game = Game()
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def initialize():

	if request.method == 'GET':
		# print('yeet')
		return render_template('main.html')

	elif request.method == 'POST':

		# print('yerr')
		keys = list(request.form.keys())

		print(keys)

		for key in keys:
			player_dict[int(key)] = Player(request.form[key])

		game.num_players = len(keys)

		return render_template('settings.html')


@app.route("/play", methods=['POST'])
def play():

	# Process Settings and Update Player Dict and Game Object
	print(request.form)
	for key in list(request.form.keys()):
		settings_dict[key] = request.form[key]
		if key == 'initial_capital':
			for pl in player_dict:
				player_dict[pl].capital = int(request.form[key])

	return render_template('play.html')


@app.route("/loop", methods=['POST'])
def loop():

	
	data = request.get_json()
	# print(data)

	d = {}
	if data['state'] == 'not started':
		curr_player = 0


	d = {}	
	player = player_dict[curr_player]
	d['current_player'] = curr_player
	d['player_name'] = player.name
	d['position'] = player.position
	d['capital'] = player.capital


	return jsonify(d)


@app.route("/roll", methods=['POST'])
def roll():

	data = request.get_json()
	# print(data)


	player = player_dict[data['current_player']]
	roll_num = np.random.randint(1, NUM_DICE * DICE_SIDES)

	data['roll_num'] =  roll_num

	new_position = data['position'] + data['roll_num']
	if new_position >= BOARD_SQUARES:
		new_position = new_position % BOARD_SQUARES

	data['position'] = player.position = new_position

	return jsonify(data)


@app.route("/action", methods=['POST'])
def action():

	data = request.get_json()
	print(data)

	# Map current Game State and Player state to potential actions
	# Leaving blank for now 


	next_player = (data['current_player'] + 1 ) % game.num_players
	player = player_dict[next_player]

	d = {}
	d['current_player'] = next_player
	d['player_name'] = player.name
	d['position'] = player.position
	d['capital'] = player.capital
	
	return jsonify(d)	




if __name__ == '__main__':
	
	app.run(debug=True)