def fboard(): # This function prints out the board all pretty like! 
  	for r in board:
		print ' '.join(map(str, r))
  	print

def safe(r, c): # This checks to see if the (row, col) combo if safe from attack.
	return not any([(board[x][y]) for x in range(N) for y in range(N) if x+y == r+c or y-x == c-r or y == c or x == r])

def solve(col): # This is where the magic happens kids! 
	global count
	if col >= N:
		return
	for row in range(N):
		if safe(row, col):
			board[row][col] = 1
			if col == N-1:
				fboard()
				count += 1
				board[row][col] = 0
				return
			solve(col+1)
			board[row][col] = 0

count 	= 0
N 		= 8
board 	= [[0 for x in range(N)] for y in range(N)] # This makes an N x N board.
solve(0)

print "The total number of solutions is {}.".format(count)

