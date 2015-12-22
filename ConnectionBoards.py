import sys
sys.setrecursionlimit(1500)


class Board(object):
	"""Base Board class.  All extensions need a gameOver, legitMove, and randomMove"""
	dash = "-"
	A = "A"
	B = "B"

	def __init__(self):
		self.boardDimension = 3
		self.pieces = {}
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				self.pieces[(x,y)] = Board.dash

	def printBoard(self):
		y = self.boardDimension - 1
		while y >= 0:
			partialString = str(y) + " | "
			for x in range(self.boardDimension):
				partialString += self.pieces[(x, y)] + " "
			y -= 1
			print(partialString)

		secondBottom = "    "
		for x in range(self.boardDimension):
			secondBottom += "__"
		print(secondBottom)
		bottomLine = "    "
		for x in range(self.boardDimension):
			bottomLine += str(x) + " "
		print(bottomLine)

	def placePiece(self, loc, player):
		self.pieces[loc] = player

	def removePiece(self, loc):
		self.pieces[loc] = Board.dash

	def getEmptySquares(self):
		emptySquares = []
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				if self.pieces[(x,y)] == Board.dash:
					emptySquares.append((x,y))
		return emptySquares	


class ConnectionBoard(Board):
	ticTacToe = "ticTacToe"
	connectFour = "connectFour"
	megaTicTacToe = "megaTicTacToe"
	tie = "Tie"

	def __init__(self, game):
		self.game = game
		self.boardDimension = 3
		self.connectionLength = 3
		self.diagonalConnectionsAllowed = True
		self.gravity = False

		if game == ConnectionBoard.connectFour:
			self.connectionLength = 4
			self.boardDimension = 6
			self.gravity = True
		elif game == ConnectionBoard.megaTicTacToe:
			self.boardDimension = 8
			self.diagonalConnectionsAllowed = False

		self.pieces = {}
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				self.pieces[(x,y)] = Board.dash

	#returns a new ConnectionBoard object that is a copy of self
	def boardCopy(self):
		copiedBoard = ConnectionBoard(self.game)

		#TODO: Do this portion in constant time
		copiedBoard.pieces = {}
		for piece in self.pieces:
			copiedBoard.pieces[piece] = self.pieces[piece]
		
		return copiedBoard

	#returns a ConnectionBoard that is a successor to this one where player makes move
	def generateSuccessor(self, player, move):
		successorState = self.boardCopy()
		if successorState.legalMove(move):
			successorState.placePiece(move, player)
		else:
			print("error with the successorState")
		return successorState

	def legalMove(self, loc):
		(x, y) = loc
		return self.legitMove(x, y)

	def legitMove(self, x, y):
		if x >= self.boardDimension or x < 0 or y >= self.boardDimension or y < 0:
			return False

		if self.pieces[(x,y)] == Board.dash:
			if self.gravity == False:
				return True
			elif y == 0 or self.pieces[(x,y-1)] != Board.dash:
				return True
		return False

	def gameOver(self):
		answer = self.checkForConnections()
		if answer:
			return answer
		if len(self.getEmptySquares()) <= 0:
			return ConnectionBoard.tie
		return False

	def checkForConnections(self):
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				if self.pieces[(x,y)] != Board.dash:
					if self.allConnectionsTest(x,y):
						return self.pieces[(x,y)]
		return False

	def allConnectionsTest(self, x, y):
		if self.connectionTest(x, y, self.pieces[(x,y)], 1, 0, self.connectionLength):
			return True
		if self.connectionTest(x, y, self.pieces[(x,y)], -1, 0, self.connectionLength):
			return True
		if self.connectionTest(x, y, self.pieces[(x,y)], 0, 1, self.connectionLength):
			return True
		if self.connectionTest(x, y, self.pieces[(x,y)], 0, -1, self.connectionLength):
			return True
		if self.diagonalConnectionsAllowed:
			if self.connectionTest(x, y, self.pieces[(x,y)], 1, 1, self.connectionLength):
				return True
			if self.connectionTest(x, y, self.pieces[(x,y)], -1, 1, self.connectionLength):
				return True
			if self.connectionTest(x, y, self.pieces[(x,y)], 1, -1, self.connectionLength):
				return True
			if self.connectionTest(x, y, self.pieces[(x,y)], -1, -1, self.connectionLength):
				return True
		return False
					
	def connectionTest(self, x, y, player, dx, dy, numPiecesTillConnection):
		if numPiecesTillConnection <= 0:
			return True
		if self.pieces.get((x,y)) != player:
			return False
		return self.connectionTest(x+dx, y+dy, player, dx, dy, numPiecesTillConnection-1)
	
	#returns a list of locations of possible actions (locations are tuples: (x,y) )	
	def possibleActions(self):
		if self.game == ConnectionBoard.connectFour:
			empty = self.getEmptySquares()
			actions = []
			for loc in empty:
				if self.legalMove(loc):
					actions.append(loc)
			return actions
		return self.getEmptySquares()





