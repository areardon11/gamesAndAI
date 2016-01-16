import ConnectionBoards
import theLgame
import Agent

def playConnectionGame(game):
	string = False
	while not string:
		string = raw_input("Please choose the number of players: ")
		if not string:
			print("Please choose the number of players to be 0, 1, or 2")
	if string == "0":
		playConnectionGameComputer(game)
	if string == "1":
		playConnectionGameMixed(game)
	if string == "2":
		playConnectionGameHumans(game)

	print("Thanks for playing!")

def playConnectionGameComputer(game):
	board = ConnectionBoards.ConnectionBoard(game)
	gameOver = False
	AgentA = Agent.ConnectionRandomAgent(ConnectionBoards.Board.A)
	AgentB = Agent.ConnectionRandomAgent(ConnectionBoards.Board.B)
	while gameOver == False:
		AgentA.takeTurn(board)
		gameOver = bookkeeping(board)
		if gameOver:
			break

		AgentB.takeTurn(board)
		gameOver = bookkeeping(board)

def playConnectionGameMixed(game):
	board = ConnectionBoards.ConnectionBoard(game)

	while True:
		difficulty = raw_input("Please select a difficulty ('easy' or 'hard'): ")
		if difficulty == 'easy':
			AgentB = Agent.ConnectionRandomAgent(ConnectionBoards.Board.B)
			break
		if difficulty == 'hard':
			AgentB = Agent.ConnectionIntelligentAgent(ConnectionBoards.Board.B, ConnectionBoards.Board.A, board.depth)
			break
		print("That was not one of the options (no quotes)")

	board.printBoard()
	print("This is the board.  The bottom-left corner is '0 0'")
	gameOver = False
	while gameOver == False:
		humanTurnConnection(board, ConnectionBoards.Board.A)
		gameOver = bookkeeping(board)
		if gameOver:
			break

		AgentB.takeTurn(board)
		gameOver = bookkeeping(board)

def playConnectionGameHumans(game):
	board = ConnectionBoards.ConnectionBoard(game)
	board.printBoard()
	print("This is the board.  The bottom-left corner is '0 0'")
	gameOver = False
	while gameOver == False:
		humanTurnConnection(board, ConnectionBoards.Board.A)
		gameOver = bookkeeping(board)
		if gameOver:
			break

		humanTurnConnection(board, ConnectionBoards.Board.B)
		gameOver = bookkeeping(board)

def humanTurnConnection(board, player):
	move = None
	while not move:
		potMove = raw_input("Please enter 'x y' for your move: ")
		moveList = None
		try:
			moveList = [int(x) for x in potMove.split()]
			if len(moveList) < 2:
				continue
		except Exception, e:
			print("Try again.  Make sure you are only typing 2 integers separated by spaces.")
			continue
		if board.legitMove(moveList[0], moveList[-1]):
			move = (moveList[0], moveList[1])
		else:
			print("That is not a valid move (The x-y coordinates are indexed at 0)")
	board.placePiece(move, player)

		

def bookkeeping(board):
	board.printBoard()
	gameOver = board.gameOver()
	print("GAMEOVER? " + str(gameOver))
	return gameOver

def playTicTacToe():
	playConnectionGame(ConnectionBoards.ConnectionBoard.ticTacToe)

def playConnectFour():
	playConnectionGame(ConnectionBoards.ConnectionBoard.connectFour)

def playMegaTicTacToe():
	playConnectionGame(ConnectionBoards.ConnectionBoard.megaTicTacToe)

def main():
	print("Welcome to the personal game center!")

	while True:
		keepPlaying = True
		print("options: ticTacToe megaTicTacToe connectFour")
		print("Please type in which game you would like to play and hit enter:")
		choice = raw_input()

		while keepPlaying:
			if choice == "ticTacToe" or choice == "t":
				playTicTacToe()
			elif choice == "megaTicTacToe" or choice == "m":
				playMegaTicTacToe()
			elif choice == "connectFour" or choice == "c":
				playConnectFour()
			else:
				print("That is not a recognized game, please type in the game exactly as shown")
				break
			
			response = raw_input("Keep Playing? Type 'yes' or 'no': ")		
			if response == "no" or response == "n":
				keepPlaying = False

if __name__ == "__main__":
	main()

