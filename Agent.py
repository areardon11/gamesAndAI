import ConnectionBoards
import itertools
import random
import math

class Agent(object):
	"""Each of the Agents that extend this class will pick a move, but also have 
	methods to then actually make the move and alter the board state"""
	def __init__(self, player):
		self.player = player


class ConnectionRandomAgent(Agent):
	def __init__(self, player):
		super(ConnectionRandomAgent, self).__init__(player)

	def move(self, board):
		actions = board.possibleActions()
		action = actions[int(math.floor(random.random()*len(actions)))]
		print("Player " + self.player + " has chosen the move " + str(action))
		return action

	def takeTurn(self, board):
		loc = self.move(board)
		board.placePiece(loc, self.player)


class ConnectionIntelligentAgent(Agent):
	utilityDiscount = .999

	def __init__(self, player, opponent):
		super(ConnectionIntelligentAgent, self).__init__(player)
		self.opponent = opponent

	def move(self, board):
		action = self.minimax(board, 4)
		print("Player " + self.player + " has chosen the move " + str(action))
		return action

	def takeTurn(self, board):
		loc = self.move(board)
		board.placePiece(loc, self.player)

	def utility(self, state):
		gameOver = state.gameOver()
		if gameOver == self.player:
			return 1
		if gameOver == ConnectionBoards.ConnectionBoard.tie:
			return 0
		if gameOver == False:
			return self.boardEvaluation()
		return -1

	def boardEvaluation(self):
		return 0

	#does the minimax operation
	def minimax(self, board, maxDepth):
		# if self.player == ConnectionBoards.Board.A:
		currMax = float('-inf')
		currBestAction = None
		for action in board.possibleActions():
			successor = board.generateSuccessor(self.player, action)
			value = self.minValue(successor, maxDepth)
			if value >= currMax:
				currMax = value
				currBestAction = action
		print(currMax)
		return currBestAction

	def minValue(self, state, depth):
		if state.gameOver() or depth <= 0:
			return self.utility(state)
		v = float('inf')
		for action in state.possibleActions():
			successorState = state.generateSuccessor(self.opponent, action)
			# successorState.printBoard()
			v = min(v, self.maxValue(successorState, depth))
		return v

	def maxValue(self, state, depth):
		if state.gameOver() or depth <= 0:
			return self.utility(state)
		v = float('-inf')
		for action in state.possibleActions():
			successorState = state.generateSuccessor(self.player, action)
			v = max(v, self.utilityDiscount*self.minValue(successorState, depth-1))
		return v



