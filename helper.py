import os
import pandas as pd
from config import * 


cwd = os.getcwd()
player_dict = {}
settings_dict = {}

class Player:

	def __init__(self, name):
		self.name = name
		self.position = 0
		self.capital = 0


class Game:

	def __init__(self):
		self.current_player = 0
		self.num_players = 0  
		self.board = self.Board()


	class Board:

		def __init__(self):
			self.board_squares = BOARD_SQUARES
			self.num_dice = 2
			self.dice_sides = 6

			df = pd.read_csv(os.path.join(cwd, 'board.csv'))
			self.squares = {index: self.Square(row) for index, row in df.iterrows()}
			self.monopolies = {mp: self.Monopoly(mp, df[df['monopoly'] == mp]) for mp in df['monopoly'].unique() 
																				if mp != 'None'}

		class Square:

			def __init__(self, data):

				class Rent:
					def __init__(self,  data):

						self.structure = None
						if data['rent']:
							self.structure = {index: val for index, val in data.iteritems() 
															if 'rent' in index}

				self.name = data['name']
				self.type = data['class']
				self.position = data['position']
				self.monopoly = data['monopoly']
				self.price = data['price']
				self.build_cost = data['build_cost']
				self.rent = Rent(data)
				self.tax = data['tax']

				self.owner = None
				self.houses = None


		class Monopoly:

			def __init__(self, name, data):

				self.name = data['monopoly'].unique()[0]
				self.type = data['class'].unique()[0]
				self.size = data['monopoly_size'].unique()[0]
				self.positions = data['position'].to_dict()


	def player_action(self, data):

		player_id = data['current_player']
		player = player_dict[player_id]
		player_position = player.position

		# Potential Actions Related to Landing on Square

		board = self.board

		square = board.squares[player_position]
		if square.type in ['Street', 'Railroad', 'Utility']:

			if square.owner:

				if square.owner != player_id:

					landowner = player_dict[square.owner]

					rent = square.rent.structure[f'rent_house_{square.houses}'] if squares.house else square.rent.structure['rent']

			else:

				d = {'name': square.name, 
					 'monopoly': square.monopoly, 
					 'price': square.price}

	 	# Potential Actions Related to Player Balance Sheet

	 		# Building Houses on Monopoly Property

	 		# Trading Property
	 		# Buying/Selling Financial Assets
	 			# Debt
	 				# Sovereign Yield Curve
	 				# Credit Market
	 			# Equity
	 				# IPO
	 				# Secondary Market
	 			# Commodity Futures
	 				# Housing Materials
	 			# Options
	 				# Rights on Property/Monopoly
	 				# Rights regarding Equity/Credit Sales


		else:

			if square.type == 'Idle':
				x = 1

			elif square.type == 'Chest':
				x = 1

			elif square.type == 'Tax':
				x = 1

			elif square.type == 'Chance':
				x = 1




		d = {}

		return d



class Market:

	def __init__(self, name):
		self.name = name





class Markets:


	def __init__(self):
		self.markets = {'bond': self.BondMarket()}


	def update(self):
		for market in self.markets:
			self.markets[market].update()
		return


	class BondMarket(Market):

		def __init__(self):
			super().__init__('Bond')


		def update(self):
			return


		class Sovereign:

			def __init__(self):
				self.x = 1


			class YieldCurve:

				def __init__(self):
					self.maturities = YIELD_CURVE_MATURITIES

					









	



		












