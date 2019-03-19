#Tech challenge
import copy
grid = [
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,2],
]
master_path = ''
test_path = ''
def slither(mystring, x, y, test_path):
	# global test_path
	# grid = [[0 for col in range(5)] for row in range(5)]
	if grid[x][y] == 2:
		master_path = test_path
		return True
	elif grid[x][y] == 1 or 0 >= x >= 4 or 0 >= y >= 4:
		return False

	if mystring[0] == '?':
		mystring_r = copy.deepcopy(mystring)
		mystring_l = copy.deepcopy(mystring)
		mystring_u = copy.deepcopy(mystring)
		mystring_d = copy.deepcopy(mystring)
		mystring[0].pop(0)
		# if slither(mystring_r, x, y+1, test_path) or slither(mystring_l, x, y-1, test_path) or slither(mystring_u, x-1, y, test_path) or slither(mystring_d, x+1, y, test_path):
		if slither(mystring_r, x, y, test_path) or slither(mystring_l, x, y, test_path) or slither(mystring_u, x, y, test_path) or slither(mystring_d, x, y, test_path):
			return True
	else:
		test_path += mystring[0]
		if mystring[0] == 'r':
			mystring.pop()
			slither(mystring, x, y+1)
		elif mystring[0] == 'l':
			mystring.pop()
			slither(mystring, x, y-1)
		elif mystring[0] == 'u':
			mystring.pop()
			slither(mystring, x-1, y)
		elif mystring[0] == 'd':
			mystring.pop()
			slither(mystring, x+1, y)

	# grid_r
	# grid_versions.append(grid)
	# path_coordinates = []
	# testX = 0
	# testY = 0
	# path = ''
	# grid[0][0]=1

	# possible_moves={
	# 	'r':(0,1),
	# 	'l':(0,-1),
	# 	'u':(-1,0),
	# 	'd':(1,0)
	# }

	# def question_mark_simulation():
	# 	#attempting to call test all the different versions of the rest of the string
	# 	nonlocal grid
	# 	if grid[4][4] == 1:
	# 		return
	# 	for move in possible_moves:
	# 		add_test_direction(move)
	# 	# if mystring[letter + 1] =='?':
	# 	# 	question_mark_simulation()

	# def confirmed_direction(direction):
	# 	nonlocal possible_moves
	# 	nonlocal testX
	# 	nonlocal testY
	# 	nonlocal path
	# 	nonlocal grid

	# 	xDelta = possible_moves[letter][0] #the change in coordinates to the next move
	# 	yDelta = possible_moves[letter][1]

	# 	#check if move is in the confines of the grid
	# 	if 0 <= (testX + xDelta) <= 4 and 0 <= (testY + yDelta) <= 4:
	# 		#check if the future space is already occupied
	# 		if grid[testX + xDelta][testY + yDelta] != 1:
	# 			#move to that coordinate
	# 			testX += xDelta
	# 			testY += yDelta
	# 			#mark grid at coordinate
	# 			grid[testX][testY] = 1
	# 			#add direction to path
	# 			path += direction
	# 	return

	# def add_test_direction(direction):
	# 	nonlocal testX
	# 	nonlocal testY
	# 	nonlocal path
	# 	nonlocal grid
	# 	#win condition
	# 	if grid[4][4] == 1:
	# 		return
	# 	nextX = testX + possible_moves[direction][0]
	# 	nextY = testY + possible_moves[direction][1]
	# 	if nextX > 4 or nextY >4:
	# 		return
	# 	#making sure the square hasnt been visited yet
	# 	if grid[nextX][nextY] == 0:
	# 		# making sure the next square isnt outside the boundaries of the grid
	# 		if 4 >= nextX >= 0 and 4 >= nextY >= 0:
	# 			#if it is safe, set the next spot traveled
	# 			testX = nextX
	# 			testY = nextY
	# 			grid[testX][testY]=1
	# 			path += direction
	# 	else:
	# 		return
	# 	print("testX: "+str(testX) +" testY: " +str(testY))

	# #current issue is that when I get to a ? believe im iterating
	# #through all the options for that ? in one go before moving to the next letter
	# for letter in mystring:
	# 	if letter == '?':
	# 		question_mark_simulation()
	# 	else:
	# 		# add_test_direction(letter)
	# 		confirmed_direction(letter)
	# print(path)
	# print(grid[0])
	# print(grid[1])
	# print(grid[2])
	# print(grid[3])
	# print(grid[4])



import boto3

BUCKET_NAME = 'tensorchallenge'
KEY = 'slitherTest.py'

s3 = boto3.resource('s3')

s3.Bucket(BUCKET_NAME).download_file(KEY, 'slitherTest.py')

import slitherTest
if slither(slitherTest.test1.split(), 0, 0, test_path): #Expected result: rrdrdrdd
	print(master_path)
# slither(slitherTest.test2)
# slither(slitherTest.test3)
