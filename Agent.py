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

	def __init__(self, player, opponent, depth):
		super(ConnectionIntelligentAgent, self).__init__(player)
		self.opponent = opponent
		self.depth = depth

	def move(self, board):
		action = self.minimaxAB(board, self.depth)
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
		return currBestAction

	def minValue(self, state, depth):
		if state.gameOver() or depth <= 0:
			return self.utility(state)
		v = float('inf')
		for action in state.possibleActions():
			successorState = state.generateSuccessor(self.opponent, action)
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


	#does the minimax operation with alpha beta pruning
	def minimaxAB(self, board, maxDepth):
		alpha = float('-inf')
		beta = float('inf')
		currMax = float('-inf')
		currBestAction = None
		for action in board.possibleActions():
			successor = board.generateSuccessor(self.player, action)
			value = self.minValueAB(successor, maxDepth, alpha, beta)
			alpha = max(alpha, value)
			if value > currMax:
				currMax = value
				currBestAction = action
			print("processing . . .")
		print(currMax)
		return currBestAction

	def minValueAB(self, state, depth, alpha, beta):
		if state.gameOver() or depth <= 0:
			return self.utility(state)
		v = float('inf')
		for action in state.possibleActions():
			successorState = state.generateSuccessor(self.opponent, action)
			v = min(v, self.maxValueAB(successorState, depth-1, alpha, beta))
			if v <= alpha:
				return v
			beta = min(beta, v)
		return v

	def maxValueAB(self, state, depth, alpha, beta):
		if state.gameOver() or depth <= 0:
			return self.utility(state)
		v = float('-inf')
		for action in state.possibleActions():
			successorState = state.generateSuccessor(self.player, action)
			v = max(v, self.utilityDiscount*self.minValueAB(successorState, depth-1, alpha, beta))
			if v >= beta:
				return v
			alpha = max(alpha, v)
		return v



