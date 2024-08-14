from n_queens.board import Board
import random
import time


#converts the 2d board to a 1d list with the column that the queen is in for each row
def boardToColumn(board):
    test = board.map
    column = []
    for row in test:
        if 1 in row: 
            #check for index of queen and add it to list
            column.append(row.index(1)+1)
    return column
            
#returns the number of non attack pairs
def getColumnFitness(column):
    maxNonAttackPairs = len(column)*(len(column)-1)/2
    fitness = 0
    dict = {}
    #check for dupes
    for f in column:
        if f not in dict:
            dict[f] =1
        else:
            fitness+=1
    #check for diagonal attacks 
    for i in range(1,(len(column)-1), 2):
        #chekc diag up left
        if column[i]+1 == (column[i-1] or column[i+1]):
            fitness +=1
        #check diag up right
        if column[i]+1 == (column[i+1]):
            fitness+=1
        #check diag down left
        if column[i]-1 == (column[i-1] or column[i+1]):
            fitness +=1
        #check diag down right
        if column[i]-1== (column[i+1]):
            fitness+=1
    return (maxNonAttackPairs - fitness)
    
#crossover between two boards
def crossover(board1,board2):
    #random num for crossover
    crossoverNum = random.randint(1,len(board1)-1)
    child1 = board1[:crossoverNum] + board2[crossoverNum:]
    child2 = board2[:crossoverNum] + board1[crossoverNum:]
    return child1, child2

#pick a random num and index to mutate
def mutate(board):
    num = random.randint(1,len(board))
    index = random.randint(0,len(board)-1)
    board[index]=num
    return board

#select which boards to mutate based on probability
def mutation(board1, board2, board3, board4):
    chance = random.randint(0,100)
    #80% chance for mutation
    if chance <=20:
        #chance to mutate each board only or mutate all boards
        mutations = random.randint(1,5)
        if mutations ==1:
            mutate(board1)
        elif mutations==2:
            mutate(board2)
        elif mutations==3:
            mutate(board3)
        elif mutations==4:
            mutate(board4)
        else:
            mutate(board1)
            mutate(board2)
            mutate(board3)
            mutate(board4)
    return board1,board2,board3,board4

#genetic algorithm to solve 5 queens problem
def genetic():
    startTime= time.time()
    #make boards as 1d list
    boards = [boardToColumn(Board(5)) for i in range(8)]
    #population of boards
    population= []
    #calculate man num of non attack pairs
    maxNonAttackPairs = len(boards[0])*(len(boards[0])-1)/2

    #population of boards with their fitness number
    for x in boards:
        population.append([x, getColumnFitness(x)])
    
    #loop until there is a board with the maximum num of non attack pairs found
    while population[0][1] !=maxNonAttackPairs:
        #new generation 
        newPopulation= []

        #sort the list by fitness from highest to lowest for selection
        population.sort(key=lambda x:x[1], reverse=True)

        #selecte the best and second best to breed
        child1, child2 = crossover(population[0][0],population[1][0])

        #select the second best and third best to breed
        child3, child4 = crossover(population[1][0], population[2][0])

        #mutates all the offsprings
        child1, child2, child3, child4 = mutation(child1,child2,child3,child4)

        #append the offsprings to new generation
        newPopulation.append([child1,getColumnFitness(child1)])
        newPopulation.append([child2,getColumnFitness(child2)])
        newPopulation.append([child3,getColumnFitness(child3)])
        newPopulation.append([child4,getColumnFitness(child4)])

        #set population to new population to reloop with new generation
        population = newPopulation
    result = "Running time: " + str(round((time.time()-startTime)* 1000))+ "ms"
    return result +"\n" + printBoard(population[0][0])

#prints out the board
def printBoard(board):
    #convert to 2d array
    nBoard = [[0 for i in range(len(board))] for  i in range(len(board))]
    for i in range(len(board)):
        column = board[i]-1
        nBoard[i][column]=1
    string = ""
    #format board
    for row in nBoard:
        for element in row:
            if element ==1:
                string += "1 "
            else:
                string += "- "
        string += "\n"
    return string
 

print(genetic())
    