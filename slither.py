#Tech challenge
#[
	# [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
	# [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
	# [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
	# [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
	# [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
#]
grid = [[(row, col) for col in range(5)] for row in range(5)]

test1 = 'r?d?drdd' #Expected result: rrdrdrdd
test2 = '???rrurdr?' #Expected result: dddrrurdrd
test3 = 'drdr??rrddd?' #Expected result: drdruurrdddd

def slither(str):
	currentX = 0
	currentY = 0
	for y in grid:
		for x in y:
			if x[0] == 0:
				print(x)
	# print(grid)



slither(test1)
# slither(test2)
# slither(test3)
