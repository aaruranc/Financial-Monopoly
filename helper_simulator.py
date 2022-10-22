import os
import numpy as np
from config import *


class Language:

	def __init__(self):
		self.x = 1

class SpeechAct:

	def __init__(self):
		self.x = 1

class ASSERT(SpeechAct):

	def __init__(self):
		self.x = 1

class ASK(SpeechAct):

	def __init__(self):
		self.x = 1

class REQUEST(SpeechAct):

	def __init__(self):
		self.x = 1

class PROMISE(SpeechAct):

	def __init__(self):
		self.x = 1

class SOLICIT(SpeechAct):

	def __init__(self):
		self.x = 1

class Communication:

	def __init__(self):
		self.x = 1

class Conversation:

	def __init__(self):
		self.x = 1

	class Presupposition:

		def __init__(self):
			self.x = 1

	class Metadata:

		def __init__(self):
			self.x = 1

	class AttitudeCluster:

		def __init__(self):
			self.x = 1


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)



class Agent:

	def __init__(self, name, settings):

		self.name = name
		self.risk_tolerance = 9


		# Initialize tree representation to embed possible worlds

		# Depth Hardcoded
		# We can fix width but need to ensure that is compatible with semantic embedding
		# At each node in the tree, we iterate thorugh the range of potential actions
		# The range of [viable] actions is a relative to a given state
		# Does this require a map of a state to a range of action
		# CAn think of actions have a minimal viability instead of requireing a complete state of inforamtion
		# i.e. if {X, Y, ...} True than can reasoanbly execute Æ

		# Prior to semantic embedding, we still need to fix an arbitray container
		# Or do we need to define the language first to scope actions?

		root = Node(5)
		for i in range(settings['tree_depth']):

			# Iterate through action



	def socialize(self, counterparty_type, cpty):
		return

	def learn(self, topic):
		return

	class Action:

		def __init__(self):
			self.x = 1

		class Default:

			def __init__(self):
				self.x = 1

	class Information:

		self.x = 1

		class KnowledgeRepresentation:

			def __init__(self):
				self.x = 1

			class Atlas:

				def __init__(self):
					self.x = 1

				class History:

					def __init__(self):
						self.x = 1

					class Chain:

						def __init__(self):
							self.x = 1

			class Belief:

				def __init__(self):
					self.x = 1

		def belief_generation(self):
			return

		def semantic_mapping(self):
			return

	class Motivation:

		self.x = 1

		class Desire:

			def __init__(self):
				self.x = 1

		class Intention:

			def __init__(self):
				self.x = 1

			def KR_partition(self, KR, intention):
				return

		class Obligation:

			def __init__(self):
				self.x = 1


	class ControlLoop:

		def __init__(self):
			self.x = 1


	class Tracker:
		
		def __init__(self):
			self.x = 1

		class Entity:

			def __init__(self):
				self.x = 1
				self.cooperation_score = 0



class Plan:

	def __init__(self):
		self.x = 1

	class Goal:

		def __init__(self):
			self.x = 1

	class Role:

		def __init__(self):
			self.x = 1


class Group(Plan):

	def __init__(self):
		
		self.x = 1
		self.members = {}

	class Permissions:
		
		def __init__(self):
			self.x = 1

	class Position:
		
		def __init__(self):
			self.x = 1

	class Election:
	
		def __init__(self):
			self.x = 1

class Institution(Group):

	def __init__(self):
		self.x = 1

	class Norm:

		def __init__(self):
			self.x = 1

		class AttitudeCluster:
			def __init__(self):
				self.x = 1

		class Defection:
			def __init__(self):
				self.x = 1

		class Sanction:

			def __init__(self):
				self.x = 1

