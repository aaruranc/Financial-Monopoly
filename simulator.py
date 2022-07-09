import datetime as dtm

from config import *
from simulator_helper import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def initialize():
	now = dtm.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return f'Simulator up at {now}'



if __name__ == '__main__':
	app.run(host=SIMULATOR_HOST, port=SIMULATOR_PORT, debug=True)