import Queue

class GameNode(object):
	"""An enum-ish object for keeping track of the value of each state"""
	WIN = "win"
	LOSS = "loss"
	TIE = "tie"
	DRAW = "draw"
	UNKNOWN = "unknown"

	def __init__(self, state):
		self.state = state
		self.value = GameNode.UNKNOWN

def possibleMoves(state):
	if state < 1:
		return []
	if state == 1:
		return [-1]
	return [-1, -2]

def makeMove(state, move):
	return state + move

def primitive(state):
	return state == 0

def parents(state):
	return [state+1, state+2]

#adds the parents of state to the given queue
def addParentsToQueue(state, queue, explored):
	for parent in parents(state):
		if parent not in explored:
			queue.put(parent)

def bfsSearch(board):
	exploredDict = dict()
	frontier = Queue.Queue()
	frontier.put(board)

	while not frontier.empty() and board not in exploredDict:
		print(exploredDict)

		state = frontier.get()

		if state not in exploredDict:
			if primitive(state):
				exploredDict[state] = GameNode.LOSS
				addParentsToQueue(state, frontier, exploredDict)
			else:
				successors = []
				for move in possibleMoves(state):
					successorState = makeMove(state, move)
					successors.append(successorState)

				allSuccessorsSolved = True
				for successor in successors:
					if successor not in exploredDict:
						allSuccessorsSolved = False

				if allSuccessorsSolved:
					successorDict = dict()
					for successor in successors:
						if exploredDict[successor] not in successorDict:
							successorDict[exploredDict[successor]] = 1
						else: 
							successorDict[exploredDict[successor]] += 1

					if GameNode.LOSS in successorDict:
						exploredDict[state] = GameNode.WIN
						addParentsToQueue(state, frontier, exploredDict)
					elif successorDict.get(GameNode.WIN) >= len(successors):
						exploredDict[state] = GameNode.LOSS
						addParentsToQueue(state, frontier, exploredDict)
				else:
					for successor in successors:
						if successor not in exploredDict:
							frontier.put(successor)

	return exploredDict[board]

print(bfsSearch(10))