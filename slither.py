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
	grid[4][4]=0
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
		print(direction)
		global testX
		global testY
		global path
		if grid[4][4] == 1:
			return
		nextX = testX + possible_moves[direction][0]
		nextY = testY + possible_moves[direction][1]
		if grid[nextX][nextY] == 0:
			if 4 >= nextX >= 0 and 4 >= nextY >= 0:
				testX = nextX
				testY = nextY
				grid[testX][testY]=1
		print("testX: "+str(testX) +" testY: " +str(testY))
		path += direction

	def question_mark_check():
		#attempting to call test all the different versions of the rest of the string
		global testX
		global testY
		global path
		global grid
		if grid[4][4] == 1:
			return
		for move in possible_moves:
			add_test_direction(move)
		# if mystring[letter + 1] =='?':
		# 	question_mark_check()

	def add_test_direction(direction):
		global testX
		global testY
		global path
		global grid
		#win condition
		if grid[4][4] == 1:
			return
		nextX = testX + possible_moves[direction][0]
		nextY = testY + possible_moves[direction][1]
		#making sure the square hasnt been visited yet
		if grid[nextX][nextY] == 0:
			# making sure the next square isnt outside the boundaries of the grid
			if 4 >= nextX >= 0 and 4 >= nextY >= 0:
				#if it is safe, set the next spot traveled
				testX = nextX
				testY = nextY
				grid[testX][testY]=1
		print("testX: "+str(testX) +" testY: " +str(testY))
		path += direction

	#current issue is that when I get to a ? believe im iterating
	#through all the options for that ? in one go before moving to the next letter
	for letter in range(len(mystring)-1):
		if mystring[letter] == '?':
			question_mark_check()
		else:
			add_confirmed_directions(mystring[letter])
	print(path)
	print(grid[0])
	print(grid[1])
	print(grid[2])
	print(grid[3])
	print(grid[4])



import boto3
import botocore

BUCKET_NAME = 'tensorchallenge' # replace with your bucket name
KEY = 'slitherTest.py' # replace with your object key

s3 = boto3.resource('s3')

s3.Bucket(BUCKET_NAME).download_file(KEY, 'slitherTest.py')

import slitherTest
slither(slitherTest.test1)
# slither(test2)
# slither(test3)
