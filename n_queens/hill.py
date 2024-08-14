import random
from n_queens.board import Board
import time

#populate boards using local search, row = random row to start looping
def populateBoard(neighbors,board,row):
    #iterate through and create a new board for each element for moving queen
    for i in range(row, row+board.n_queen):
        rowIndex = i% board.n_queen
        for j in range(board.n_queen):
            #copy board
            neighbor = Board(board.n_queen)
            neighbor.map = [row[:] for row in board.get_map()] 
            #check for where 1 is and flip to 0
            if 1 in neighbor.map[rowIndex]:
                index = neighbor.map[rowIndex].index(1)
                neighbor.flip(rowIndex,index)
            #flip current element to 1
            neighbor.flip(rowIndex,j)
            neighbors.append(neighbor)
    return neighbors

#hill climbing alorithm to solve 5 queens problem
def hill_climbing():
    startTime = time.time()
    #loop until fitness is 0
    while True:
        #generate board/reset board for next iteration
        board = Board(5)
        
        #list for configurations
        neighbors = []
        randomStart = random.randint(0,board.n_queen-1)

        #generate all configurations from random start
        neighbors = populateBoard(neighbors,board,randomStart)
 
        #find the board with the lowest fitness
        bestNeighbor = min(neighbors, key=lambda x: x.get_fitness())
        
        #end loop when there's no attack pair
        if bestNeighbor.get_fitness() == 0:
            board = bestNeighbor
            string = "Running time: " + str(round((time.time()-startTime)* 1000))+ "ms"
            return string + "\n" + print_board(board)



#prints out the board
def print_board(board):
    board = board.map
    string = ""

    #format board
    for row in board:
        for element in row:
            if element ==1:
                string += "1 "
            else:
                string += "- "
        string += "\n"
    return string


print(hill_climbing())
