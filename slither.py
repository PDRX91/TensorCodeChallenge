#Tech challenge
#[
	# [1,0,0,0,0],
	# [0,0,0,0,0],
	# [0,0,0,0,0],
	# [0,0,0,0,0],
	# [0,0,0,0,1],
#]
grid = [[0 for col in range(5)] for row in range(5)]

test1 = 'r?d?drdd' #Expected result: rrdrdrdd
test2 = '???rrurdr?' #Expected result: dddrrurdrd
test3 = 'drdr??rrddd?' #Expected result: drdruurrdddd
testX = 0
testY = 0
path = ''

def slither(mystring):
	grid[0][0]=1
	grid[4][4]=2
	currentX = 0
	currentY = 0
	possible_moves={
		'r':(0,1),
		'l':(0,-1),
		'u':(-1,0),
		'd':(1,0)
	}
	global testX
	global testY
	global path

	def add_confirmed_directions(direction):
		# print(direction)
		global testX
		global testY
		global path
		if testX == 4 and testY == 4:
			return
		testX += possible_moves[direction][0]
		testY += possible_moves[direction][1]
		path += direction

	def question_mark_check():
		global testX
		global testY
		global path
		if testX == 4 and testY == 4:
			return
		for move in possible_moves:
			add_test_direction(move)
		if mystring[letter + 1] =='?':
			question_mark_check()

	def add_test_direction(direction):
		global testX
		global testY
		global path
		if testX == 4 and testY == 4:
			return
		testX += possible_moves[direction][0]
		testY += possible_moves[direction][1]
		path += direction

	for letter in range(len(mystring)-1):

		if mystring[letter] == '?':
			question_mark_check()
		else:
			add_confirmed_directions(mystring[letter])
	print(path)





slither(test1)
# slither(test2)
# slither(test3)
