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