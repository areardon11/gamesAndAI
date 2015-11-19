import random
import math

ticTacToe = "ticTacToe"
connectFour = "connectFour"
megaTicTacToe = "megaTicTacToe"

dash = "-"

class Board(object):

	def __init__(self, game):
		self.connectionLength = 3
		self.boardDimension = 3
		self.diagonalConnectionsAllowed = True
		self.gravity = False

		if game == connectFour:
			self.connectionLength = 4
			self.boardDimension = 6
			self.gravity = True
		elif game == megaTicTacToe:
			self.boardDimension = 8
			self.diagonalConnectionsAllowed = False

		self.numEmptySpaces = self.boardDimension*self.boardDimension
		self.pieces = {}
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				self.pieces[(x,y)] = dash

	def printBoard(self):
		y = self.boardDimension - 1
		while y >= 0:
			partialString = ""
			for x in range(self.boardDimension):
				partialString = partialString + self.pieces[(x, y)]
			y -= 1
			print(partialString)

	def placePiece(self, loc, player):
		self.pieces[loc] = player
		self.numEmptySpaces -= 1

	def legitMove(self, x, y):
		"""TODO: Add checks for within bounds of board here, and also that player is legit"""
		if self.pieces[(x,y)] == dash:
			if self.gravity == False:
				return True
			elif y == 0 or self.pieces[(x,y-1)] != dash:
				return True
		return False

	def gameOver(self):
		"""TODO: figure out if there is a winner"""
		if self.numEmptySpaces <= 0:
			return True
		return self.checkForConnections()

	def checkForConnections(self):
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				if self.pieces[(x,y)] != dash:
					if self.allConnectionsTest(x,y):
						return True
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

	def randomMove(self):
		if self.numEmptySpaces <= 0:
			return None
		x = math.floor(random.random()*self.boardDimension)
		y = math.floor(random.random()*self.boardDimension)
		if self.legitMove(x, y):
			return (x,y)
		else:
			return self.randomMove()

def playGame(game):
	A = "A"
	B = "B"

	board = Board(game)
	gameOver = False
	while gameOver == False:
		takeTurn(board, A)
		gameOver = bookkeeping(board)
		if gameOver:
			break

		takeTurn(board, B)
		gameOver = bookkeeping(board)

def takeTurn(board, player):
	loc = board.randomMove()
	board.placePiece(loc, player)

def bookkeeping(board):
	board.printBoard()
	gameOver = board.gameOver()
	print("GAMEOVER? " + str(gameOver))
	return gameOver

def playTicTacToe():
	playGame(ticTacToe)

def playConnectFour():
	playGame(connectFour)

def playMegaTicTacToe():
	playGame(megaTicTacToe)

		

		