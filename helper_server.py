import os
import numpy as np
import pandas as pd
from config import * 

np.random.seed(304)
cwd = os.getcwd()
player_dict = {}
settings_dict = {}

class Player:

	def __init__(self, name):
		self.name = name
		self.position = 0
		self.capital = 0
		self.orbit = 0
		self.property = {}
		self.monopoly = {}


class Game:

	def __init__(self):
		self.current_player = 0
		self.num_players = 0  
		self.board = self.Board()


	class Board:

		def __init__(self):
			self.board_squares = BOARD_SQUARES
			self.num_dice = NUM_DICE
			self.dice_sides = DICE_SIDES

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
				self.positions = list(data['position'])


	def player_actions(self, data):

		player_id = data['current_player']
		player = player_dict[player_id]
		player_position = player.position

		# Potential Actions Related to Landing on Square

		board = self.board
		square = board.squares[player_position]
		options = {}

		if square.type in ['Street', 'Railroad', 'Utility']:

			if square.owner:

				if square.owner != player_id:

					landowner = player_dict[square.owner]
					rent = square.rent.structure[f'rent_house_{square.houses}'] if square.houses else square.rent.structure['rent']
					options['rent'] = {'name': square.name,
									   'owner': square.owner, 
									   'rent': rent}


			else:

				options['buy'] = {'name': square.name, 
								  'monopoly': square.monopoly, 
								  'price': square.price}

	 	# Potential Actions Related to Player Balance Sheet
	 	# Want to Design so that this capacity is asynchronous
	 	# MAybe restrict callback here to actions tied to dice roll and leave options elsewhere
	 		# Building Houses on Monopoly Property
	 		# Trading Property
	 		# Buying/Selling Financial Assets
	 			# Debt
	 				# Sovereign Yield Curve
	 				# Credit Market
	 			# Equity
	 				# IPO
	 				# Public / Private Secondary Market
	 			# Commodity Futures
	 				# Housing Materials
	 			# Options
	 				# Rights on Property/Monopoly
	 				# Rights regarding Equity/Credit Sales

		else:

			if square.type == 'Idle': 

				# Go Money, Amount recieved should end up as a setting
				# Need to have update if passed, not just on land ***
				if player_position == 0:
					player.capital += GO_MONEY

			elif square.type == 'Chest': x = 1
			elif square.type == 'Tax': x = 1
			elif square.type == 'Chance': x = 1


		options['current_player'] = data['current_player']
		options['player_name'] = data['player_name']
		options['position'] = data['position']
		options['capital'] = data['capital']

		return options


	def process_decision(self, data):

		player_id = data['current_player']
		player = player_dict[player_id]
		player_position = player.position

		d = {}
		if 'rent' in data:

			if data['rent']['rent'] <= player.capital:


				name = data['rent']['name']
				rent = data['rent']['rent']

				player.capital -= data['rent']['rent'] 

				d['consequence'] = f'{player.name} paid {rent} on {name}'

			else:

				# Handle Bankruptcy
				print(f'{player.name} is Bankrupt !!!!')
				d['consequence'] = f'{player.name} is bankrupt'


		elif 'buy' in data:

			# Buy if Coinflip Winner
			if np.random.randint(2):
				if data['buy']['price'] <= player.capital:

					board = self.board
					square = board.squares[player_position]
					mply = square.monopoly
					monopoly = board.monopolies[mply]

					# print(vars(monopoly))

					square.owner = player_id

					name = square.name
					price = data['buy']['price']
					player.capital -= data['buy']['price']


					# positions = data['position'].to_dict()

					if monopoly in player.property:
						player.property[monopoly][square.position] = square.name

					else:
						
						player.property[monopoly] = {square.position: square.name}

					d['consequence'] = f'{player.name} bought {name} for {price}'

					# Update Monopolies 


		# print(d)
		# print(vars(player))


		next_player = (data['current_player'] + 1 ) % self.num_players
		player = player_dict[next_player]

		
		d['current_player'] = next_player
		d['player_name'] = player.name
		d['position'] = player.position
		d['capital'] = player.capital
		# d['properties'] = vars(player.property)

		return d




class Market:

	def __init__(self, name):
		self.name = name

		class Exchange:

			def __init__(self):
				self.x = 1

			class Transaction:

				def __init__(self):
					self.x = 1

				class Contract:

					def __init__(self):
						self.x = 1


class CapitalMarkets:

	def __init__(self):
		self.markets = {}

	def update(self):
		for market in self.markets:
			self.markets[market].update()
		return

	
	class Bonds(Market):

		def __init__(self):
			super().__init__('Bonds')

		def update(self):
			return


		class Sovereign:

			def __init__(self):
				self.x = 1

			class YieldCurve:

				def __init__(self):
					self.maturities = YIELD_CURVE_MATURITIES

		class Mortgage:

			def __init__(self):
				self.x = 1


		class Credit:

			def __init__(self):
				self.x = 1


		class Repo:

			def __init__(self):
				self.x = 1

	class Commodities(Market):

		def __init__(self):
			super().__init__('Bonds')


		def update(self, Bonds, Industry):
			return

	class Labor(Market):

		def __init__(self):
			super().__init__('Labor')

	class RealEstate(Market):

		def __init__(self):
			super().__init__('Real Estate')


		def update(self, Bonds, Commodities, Labor):
			return

	class Stocks(Market):

		def __init__(self):
			super().__init__('Stocks')

		class DCF:

			def __init__(self, Bonds):
				self.x = 1

		class IPO:

			def __init__(self, Bonds):
				self.x = 1

		class LBO:

			def __init__(self, Bonds):
				self.x = 1	

		def update(self, Bonds, RealEstate):
			return

	class Derivatives(Market):

		def __init__(self):
			super().__init__('Derivatives')


		def update(self, Bonds, Commodities, RealEstate, Stocks, Labor, Industry):
			return

		class Fund:

			def __init__(self):
				self.x = 1
	
		class Future:

			def __init__(self):
				self.x = 1

		class Option:

			def __init__(self):
				self.x = 1

		class Swap:

			def __init__(self):
				self.x = 1	

			class CDS:

				def __init__(self):
					self.x = 1


class Finance:

	def __init__(self):
		self.x = 1
		self.exuberance = 3		

	class Business:

		def __init__(self):
			self.x = 1

	class CentralBank:

		def __init__(self):
			self.x = 1
			self.hubris = 10
			self.easy_money = 9
			self.chairman = 'Greenspan'

		def quantitative_easing(self, Bonds):
			return 

		def rate_change(self, Bonds, magnitude=.25):
			return 

		def yield_curve_control(self, Bonds, maturity, rate):
			return 

	class InvestmentBank:

		def __init__(self):
			self.x = 1
			self.credit_creation = 7

		class PrimeBroker:

			def __init__(self):
				self.x = 1

	class Investor:

		def __init__(self):
			self.x = 1
			self.leverage = 2.5

		class PrivateEquity:

			def __init__(self):
				self.x = 1

		class VentureCapital:

			def __init__(self):
				self.x = 1

		class HedgeFund:

			def __init__(self):
				self.x = 1

		class PensionFund:

			def __init__(self):
				self.x = 1

		class ETFIssuer:

			def __init__(self):
				self.x = 1

	class MarketMaker:

		def __init__(self):
			self.x = 1
			self.arbitrageur = .9
			self.prop = .7

	class Auditor:

		def __init__(self):
			self.x = 1

	class Regulator:

		def __init__(self):
			self.x = 1


class World:

	def __init__(self):
		self.x = 1
		self.stability = 0

	class Industry:

		def __init__(self):
			self.x = 1

		class Resource:

			def __init__(self):
				self.x = 1

	class Volksgeist:

		def __init__(self):
			self.x = 1
			self.redistribution = 5

		class Government:

			def __init__(self):
				self.x = 1
				self.bribery = 4

	class Weitgeist:

		def __init__(self):
			self.x = 1
			self.natural_disaster = 3

		class GlobalWarming:

			def __init__(self):
				self.x = 1			

	class Zeitgeist:

		def __init__(self):
			self.x = 1
			self.cooperation = .8

		class Culture:

			def __init__(self):
				self.x = 1



class Settings:

	def __init__(self):

		self.initial_capital = INITIAL_CAPITAL
		self.auction = True
		self.go_around = True

