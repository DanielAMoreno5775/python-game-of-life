#Conqay's Game of Life from https://automatetheboringstuff.com/2e/chapter4/ with a few modifications
#A hash represented a living square and an empty space represents a dead square
#If a living square has two or three living neighbors, it survives
#If a dead square has three living neighbors, it comes alive
#All other squares die at the end of each round

import random, time, copy, sys
WIDTH = 60
HEIGHT = 20

game_board_count = input("How many times would you like to run this program? ")
game_board_count = int(game_board_count)
game_instance = 1

try:
	# Create a list of list for the cells:
	nextCells = []
	#Creates next board
	for x in range(WIDTH):
		column = [] # Create a new column.
		for y in range(HEIGHT):
			if random.randint(0, 1) == 0: #Creates 50/50 chance of being a living cell
				column.append('#') # Add a living cell.
			else:
				column.append(' ') # Add a dead cell.
		nextCells.append(column) # nextCells is a list of column lists.

	while game_instance <= game_board_count: # Main program loop.
		print('\n\n\n\n\n') # Separate each step with newlines.
		currentCells = copy.deepcopy(nextCells) #copies board from previous round

		# Print currentCells on the screen:
		for y in range(HEIGHT):
			for x in range(WIDTH):
				print(currentCells[x][y], end='') # Print the # or space.
			print() # Print a newline at the end of the row.

		# Calculate the next step's cells based on current step's cells:
		for x in range(WIDTH):
			for y in range(HEIGHT):
				# Get neighboring coordinates:
				# `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
				leftCoord  = (x - 1) % WIDTH
				rightCoord = (x + 1) % WIDTH
				aboveCoord = (y - 1) % HEIGHT
				belowCoord = (y + 1) % HEIGHT

				# Count number of living neighbors:
				numNeighbors = 0
				if currentCells[leftCoord][aboveCoord] == '#':
					numNeighbors += 1 # Top-left neighbor is alive.
				if currentCells[x][aboveCoord] == '#':
					numNeighbors += 1 # Top neighbor is alive.
				if currentCells[rightCoord][aboveCoord] == '#':
					numNeighbors += 1 # Top-right neighbor is alive.
				if currentCells[leftCoord][y] == '#':
					numNeighbors += 1 # Left neighbor is alive.
				if currentCells[rightCoord][y] == '#':
					numNeighbors += 1 # Right neighbor is alive.
				if currentCells[leftCoord][belowCoord] == '#':
					numNeighbors += 1 # Bottom-left neighbor is alive.
				if currentCells[x][belowCoord] == '#':
					numNeighbors += 1 # Bottom neighbor is alive.
				if currentCells[rightCoord][belowCoord] == '#':
					numNeighbors += 1 # Bottom-right neighbor is alive.

				# Set cell based on Conway's Game of Life rules:
				if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
					# Living cells with 2 or 3 neighbors stay alive:
					nextCells[x][y] = '#'
				elif currentCells[x][y] == ' ' and numNeighbors == 3:
					# Dead cells with 3 neighbors become alive:
					nextCells[x][y] = '#'
				else:
					# Everything else dies or stays dead:
					nextCells[x][y] = ' '
		time.sleep(1.1) # Add a 1.1-second pause to reduce flickering.
		game_instance += 1
except KeyboardInterrupt: #ends program if CTRL+C is entered but without the traditional error message
    sys.exit()