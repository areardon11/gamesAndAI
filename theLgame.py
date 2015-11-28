import ConnectionBoards
import itertools
import random
import math

theLgame = "theLgame"
dash = ConnectionBoards.dash
A = "A"
B = "B"
O = "O"

class LBoard(ConnectionBoards.Board):
	lPiece = "lPiece"
	dotPiece = "dotPiece"

	def __init__(self):
		self.boardDimension = 4
		self.pieces = {}
		for x in range(self.boardDimension):
			for y in range(self.boardDimension):
				self.pieces[(x,y)] = dash
		self.intializePieces()

	def intializePieces(self):
		self.pieces[(0,0)] = A
		for y in range(3):
			self.pieces[(1,y)] = A
		self.pieces[(self.boardDimension-1, self.boardDimension-1)] = B
		for y in range(3):
			self.pieces[(self.boardDimension-2, self.boardDimension-1-y)] = B
		self.pieces[(self.boardDimension-1, 0)] = O
		self.pieces[(0, self.boardDimension-1)] = O

	#inherits printBoard(self)

	def placePiece(self, loc, player):
		self.pieces[loc] = player

	def removePiece(self, loc):
		self.pieces[loc] = dash

	def gameOver(self):
		numMoves = 0
		empty = self.getEmptySquares()
		combos = itertools.combinations(empty, 4)
		for combo in combos:
			if self.legitMove(list(combo), LBoard.lPiece):
				numMoves += 1
		print("There are " + str(numMoves) + " possible moves.")
		return numMoves <= 0

	def legitMove(self, pairs, pieceType):
		for (x, y) in pairs:
			if x >= self.boardDimension or x < 0 or y >= self.boardDimension or y < 0:
				return False
			if self.pieces[(x,y)] != dash:
				return False

		if pieceType == LBoard.lPiece:
			return self.checkForLShape(pairs)
		return True

	def checkForLShape(self, pairs):
		for startPair in pairs:
			pairCopy = pairs[:]
			pairCopy.remove(startPair)
			if self.checkLStart(startPair, pairCopy):
				return True
		return False

	def checkLStart(self, startLoc, otherLocs):
		(x,y) = startLoc
		for i in range(-1, 2):
			if i == 0:
				j = -1
				while j <= 1:
					cornerLoc = (x, y+j)
					if cornerLoc in otherLocs:
						otherLocsCopy = otherLocs[:]
						otherLocsCopy.remove(cornerLoc)
						return self.checkLX(cornerLoc, otherLocsCopy, 0, j)
					j += 2
			else:
				cornerLoc = (x+i, y)
				if cornerLoc in otherLocs:
					otherLocsCopy = otherLocs[:]
					otherLocsCopy.remove(cornerLoc)
					return self.checkLY(cornerLoc, otherLocsCopy, i, 0)
		return False
		
	def checkLX(self, cornerLoc, remainingLocs):
		(x,y) = cornerLoc
		if (x+1, y) in remainingLocs and (x+2, y) in remainingLocs:
			return True
		if (x-1, y) in remainingLocs and (x-2, y) in remainingLocs:
			return True
		return False

	def checkLY(self, cornerLoc, remainingLocs):
		(x,y) = cornerLoc
		if (x, y+1) in remainingLocs and (x, y+2) in remainingLocs:
			return True
		if (x, y-1) in remainingLocs and (x, y-2) in remainingLocs:
			return True
		return False
			


