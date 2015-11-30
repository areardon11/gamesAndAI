import ConnectionBoards
import itertools
import random
import math

class Agent(object):
	"""Each of the Agents that extend this class will pick a move, but also have 
	methods to then actually make the move and alter the board state"""
	def __init__(self, player):
		self.player = player

	def move():
		return (0,0)

class ConnectionRandomAgent(Agent):
	def __init__(self, player):
		super(ConnectionRandomAgent, self).__init__(player)

	def randomMove(self, board):
		x = math.floor(random.random()*board.boardDimension)
		y = math.floor(random.random()*board.boardDimension)
		if board.legitMove(x, y):
			return (x,y)
		else:
			return self.randomMove(board)

	def takeTurn(self, board):
		loc = self.randomMove(board)
		board.placePiece(loc, self.player)

class ConnectionIntelligentAgent(Agent):
	def __init__(self, player):
		super(ConnectionIntelligentAgent, self).__init__(player)

	def move(self, board):
		if self.player == ConnectionBoards.Board.A:
			
			for action in board.possibleActions():
				pass
		else:
			
		

		