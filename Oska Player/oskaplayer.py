## oskaplayer.py
## Maayez Imam 915342727

import copy
import math

## oskaplayer takes in a board, the color of the player whose making the next move,
## and how many moves ahead my minimax search looks ahead
## it returns the best next move (the second value in the list the function minimaxB and minimaxW return)
def oskaplayer(board, color, minimax):
    ## if there are no moves to be made, return the original board
    if movegen(board, color) == board:
        return board
    if color == 'b':
        return minimaxB(board, minimax, color)[1]
    if color == 'w':
        return minimaxW(board, minimax, color)[1]
    return board


## minimaxB takes in a board, the desired depth the user wants to look, and the player's color
## this function is specifically for black players
## it uses recursion to look down all the possible nodes on one move the player can make
## it does this for all the moves the player can make
## using the minimax algorithm, it brings up either the max or min heuristic value depending on who the maximizing player is
## it returns the final heuristic value and the board of the move that value corresponds to
def minimaxB(board, depth, color):
    if (depth == 0) or movegen(board, color) == board:
        return heuristic(board, 'b'), None
    if color == 'b':
        value = -math.inf
        bestMove = board
        for i in movegen(board, color):
            tempMax, _ = minimaxB(i, depth - 1, 'w')
            if tempMax > value:
                value = tempMax
                bestMove = i
        return value, bestMove

    else:
        value = math.inf
        best = board
        for j in movegen(board, color):
            tempMin, _ = minimaxB(j, depth - 1, 'b')
            if tempMin < value:
                value = tempMin
                best = j
        return value, best


## minimaxW takes in a board, the desired depth the user wants to look, and the player's color
## this function is specifically for white players
## it uses recursion to look down all the possible nodes on one move the player can make
## it does this for all the moves the player can make
## using the minimax algorithm, it brings up either the max or min heuristic value depending on who the maximizing player is
## it returns the final heuristic value and the board of the move that value corresponds to
def minimaxW(board, depth, color):
    if (depth == 0) or movegen(board, color) == board:
        return heuristic(board, 'w'), None
    if color == 'w':
        value = -math.inf
        bestMove = board
        for i in movegen(board, color):
            tempMax, _ = minimaxB(i, depth - 1, 'b')
            if tempMax > value:
                value = tempMax
                bestMove = i
        return value, bestMove

    else:
        value = math.inf
        best = board
        for j in movegen(board, color):
            tempMin, _ = minimaxB(j, depth - 1, 'w')
            if tempMin < value:
                value = tempMin
                best = j
        return value, best

## heuristic function takes in a board and the color of the player whose turn it is
## the heuristic I chose to use is calculated as followed:
## number of player's pieces left MINUS number of opponent pieces left
## PLUS
## the total number of rows away from the starting row for all the player's pieces
## MINUS
## the total number of rows away from starting row for all the opponent's pieces
## for example, a board that looks like ['www-', '--b', '--', '---', 'b-bb'] would have a heuristic of 4 for 'b' player
## this calculated by:  (4 - 3) + ((3 + 0 + 0 + 0) - (0 + 0 + 0)) = 1 + 3 = 4
## it checks to see if the player is a winning state or losing state
## if the player is in a winning state, it returns a heuristic value of 100
## if the player is in a losing state, it returns a heuristic value of -100
## heuristic function returns the calculated heuristic value for the chosen player
def heuristic(board, color):
    state = toArray(board)
    ## calculate heuristic for black players
    if color == 'b':
        if movegen(board, 'b') == board:
            h = 100
            return h
        if movegen(board, 'w') == board:
            h = -100
            return h
        ## calculate heuristic for black moves
        numB = sum(i.count('b') for i in state)
        numW = sum(i.count('w') for i in state)
        firstRow = len(board[0])
        rows = (2 * firstRow) - 3
        numRowsAwayB = 0
        numRowsAwayW = 0
        for i, j in enumerate(state):
            for x, y in enumerate(j):
                if y == 'b':
                    numRowsAwayB = numRowsAwayB + ((rows - 1) - i)
        for i, j in enumerate(state):
            for x, y in enumerate(j):
                if y == 'w':
                    numRowsAwayW = numRowsAwayW + i
        h = (numB - numW) + (numRowsAwayB - numRowsAwayW)
        return h

    ## calculate heuristic for white players
    if color == 'w':
        if movegen(board, 'w') == board:
            h = 100
            return h
        if movegen(board, 'b') == board:
            h = -100
            return h
        ## calculate heuristic for white moves
        numW = sum(i.count('w') for i in state)
        numB = sum(i.count('b') for i in state)
        firstRow = len(board[0])
        rows = (2 * firstRow) - 3
        numRowsAwayW = 0
        numRowsAwayB = 0
        for i, j in enumerate(state):
            for x, y in enumerate(j):
                if y == 'w':
                    numRowsAwayW = numRowsAwayW + i
        for i, j in enumerate(state):
            for x, y in enumerate(j):
                if y == 'b':
                    numRowsAwayB = numRowsAwayB + ((rows - 1) - i)
        h = (numW - numB) + (numRowsAwayW - numRowsAwayB)
        return h


## movegen function returns all the possible moves that a player can make
## with the given board
## first argument is a board
## second argument is the player's turn who is next in lowercase letter ('b' or 'w')
## if nextTurn is 'b' then it shows all the moves the black player can make
## if nextTurn is 'w' then it shows all the moves the white player can make
def movegen(board, nextTurn):
    result = []
    if nextTurn == 'b':
        result = blackMove(board)
        # result = generateNewBlackBoard(board)
        return result
    elif nextTurn == 'w':
        result = whiteMove(board)
        # result = generateNewWhiteBoard(board)
        return result
    return result


## blackMove takes in the current board as an argument
## it returns a list of the possible black moves
## it iterates through the elements in the board and finds the Bs
## goes through if statements to check whether the B is on the top half of the board or the bottom half
## if its on the top half it does one set of moves
## if its on the bottom half it does another set of moves
## more if statements to check if the piece is on the leftmost or rightmost side of the row
## if it is it does one set of moves
## more if statements to check if the piece is in the middle of the row
## if it is it does another set of moves
## for every set of moves it can do, it creates a new board and appends it to a list
def blackMove(board):
    result = []
    state = toArray(board)
    tempState = copy.deepcopy(state)
    tempState1 = copy.deepcopy(state)
    tempState2 = copy.deepcopy(state)
    tempState3 = copy.deepcopy(state)
    tempState4 = copy.deepcopy(state)
    tempState5 = copy.deepcopy(state)
    tempState6 = copy.deepcopy(state)
    tempState7 = copy.deepcopy(state)
    tempState8 = copy.deepcopy(state)
    tempState9 = copy.deepcopy(state)
    tempState10 = copy.deepcopy(state)
    tempState11 = copy.deepcopy(state)
    tempState12 = copy.deepcopy(state)
    tempState13 = copy.deepcopy(state)
    tempState14 = copy.deepcopy(state)
    n = sum(i.count('b') for i in state)
    numW = sum(i.count('w') for i in state)
    # print(n)
    ## check if player has no pieces left
    if (numW == 0):
        return board
    if (n == 0):
        return board
    firstRow = len(board[0])
    rows = (2*firstRow) - 3
    middle = n - 2
    count = 0
    # print(tempState1)
    # state = toString(state)
    for i, j in enumerate(state):
        for x, y in enumerate(j):
            if y == 'b':
                if i == 0:
                    count = count + 1
                ## checks if all the pieces are on the opponent's side
                if count == n:
                    return board
                # print(i, x)
                if i > n - 2:
                    ## bottom half of board
                    if x == 0:
                        ## leftmost piece
                        if tempState1[i - 1][x] == '-':
                            # move up one row
                            tempState1[i][x], tempState1[i - 1][x] = tempState1[i - 1][x], tempState1[i][x]
                            result.append(toString(tempState1))
                        elif (tempState1[i - 1][x] == 'w') & (tempState1[i - 2][x] == '-') & (i - 2 >= n - 2):
                            ## jump over piece two rows up
                            tempState1[i][x], tempState1[i - 2][x] = tempState1[i - 2][x], tempState1[i][x]
                            tempState1[i - 1][x] = '-'
                            result.append(toString(tempState1))
                        elif (tempState1[i - 1][x] == 'w') & (tempState1[i - 2][x + 1] == '-') & (i - 2 < n - 2):
                            ## jump over piece two rows up
                            tempState1[i][x], tempState1[i - 2][x + 1] = tempState1[i - 2][x + 1], tempState1[i][x]
                            tempState1[i - 1][x] = '-'
                            result.append(toString(tempState1))
                    if tempState[i][-1] == 'b':
                        ## rightmost piece
                        if tempState2[i - 1][-1] == '-':
                            # move up one row
                            tempState2[i][-1], tempState2[i - 1][-1] = tempState2[i - 1][-1], tempState2[i][-1]
                            result.append(toString(tempState2))
                        elif (tempState2[i - 1][-1] == 'w') & (tempState2[i - 2][-1] == '-') & (i - 2 >= n - 2):
                            ## jump over piece two rows up
                            tempState2[i][-1], tempState2[i - 2][-1] = tempState2[i - 2][-1], tempState2[i][-1]
                            tempState2[i - 1][-1] = '-'
                            result.append(toString(tempState2))
                        elif (tempState2[i - 1][-1] == 'w') & (tempState2[i - 2][-2] == '-') & (i - 2 < n - 2):
                            ## jump over piece two rows up
                            tempState2[i][-1], tempState2[i - 2][-2] = tempState2[i - 2][-2], tempState2[i][-1]
                            tempState2[i - 1][-1] = '-'
                            result.append(toString(tempState2))
                    if (i == rows - 1) & (x == 1):
                        ## second element middle piece in last row
                        if tempState7[i - 1][x - 1] == '-':
                            ## move up diagonally left
                            tempState7[i][x], tempState7[i - 1][x - 1] = tempState7[i - 1][x - 1], tempState7[i][x]
                            result.append(toString(tempState7))
                        if tempState8[i - 1][x] == '-':
                            ## move up diagonally right
                            tempState8[i][x], tempState8[i - 1][x] = tempState8[i - 1][x], tempState8[i][x]
                            result.append(toString(tempState8))
                        elif (tempState8[i - 1][x] == 'w') & (tempState8[i - 2][x] == '-'):
                            ## jump over piece diagonally right
                            tempState8[i][x], tempState8[i - 2][x] = tempState8[i - 2][x], tempState8[i][x]
                            tempState8[i - 1][x] = '-'
                            result.append(toString(tempState8))
                    if (i == rows - 1) & (x == 2):
                        ## third element middle piece in last row
                        if tempState9[i - 1][x - 1] == '-':
                            ## move up diagonally left
                            tempState9[i][x], tempState9[i - 1][x - 1] = tempState9[i - 1][x - 1], tempState9[i][x]
                            result.append(toString(tempState9))
                        elif (tempState9[i - 1][x - 1] == 'w') & (tempState9[i - 2][x - 2] == '-'):
                            ## jump over piece diagonally left
                            tempState9[i][x], tempState9[i - 2][x - 2] = tempState9[i - 2][x - 2], tempState9[i][x]
                            tempState9[i - 1][x - 1] = '-'
                            result.append(toString(tempState9))
                        if tempState10[i - 1][x] == '-':
                            ## move up diagonally right
                            tempState10[i][x], tempState10[i - 1][x] = tempState10[i - 1][x], tempState10[i][x]
                            result.append(toString(tempState10))
                    if (i == rows - 2) & (x == 1):
                        ## middle piece in second last row
                        if tempState11[i - 1][x - 1] == '-':
                            ## move up diagonally left
                            tempState11[i][x], tempState11[i - 1][x - 1] = tempState11[i - 1][x - 1], tempState11[i][x]
                            result.append(toString(tempState11))
                        elif (tempState11[i - 1][x - 1] == 'w') & (tempState11[i - 2][x - 1] == '-'):
                            ## jump over piece diagonally left
                            tempState11[i][x], tempState11[i - 2][x - 1] = tempState11[i - 2][x - 1], tempState11[i][x]
                            tempState11[i - 1][x - 1] = '-'
                            result.append(toString(tempState11))
                        if tempState12[i - 1][x] == '-':
                            ## move up diagonally right
                            tempState12[i][x], tempState12[i - 1][x] = tempState12[i - 1][x], tempState12[i][x]
                            result.append(toString(tempState12))
                        elif (tempState12[i - 1][x] == 'w') & (tempState12[i - 2][x + 1] == '-'):
                            ## jump over piece diagonally right
                            tempState12[i][x], tempState12[i - 2][x + 1] = tempState12[i - 2][x + 1], tempState12[i][x]
                            tempState12[i - 1][x] = '-'
                            result.append(toString(tempState12))

                if i <= n - 2:
                    ## top half of board
                    if x == 0:
                        ## leftmost piece
                        if (tempState3[i - 1][x] == '-') & (i != 0):
                            ## move diagonally up left
                            tempState3[i][x], tempState3[i - 1][x] = tempState3[i - 1][x], tempState3[i][x]
                            result.append(toString(tempState3))
                        elif (tempState3[i - 1][x] == 'w') & (tempState3[i - 2][x] == '-') & (i - 1 != 0) & (i != 0):
                            ## jump over piece diagonally up left
                            tempState3[i][x], tempState3[i - 2][x] = tempState3[i - 2][x], tempState3[i][x]
                            tempState3[i - 1][x] = '-'
                            result.append(toString(tempState3))
                        if (tempState4[i - 1][x + 1] == '-') & (i != 0):
                            ## move diagonally up right
                            tempState4[i][x], tempState4[i - 1][x + 1] = tempState4[i - 1][x + 1], tempState4[i][x]
                            result.append(toString(tempState4))
                        elif (tempState4[i - 1][x + 1] == 'W') & (tempState4[i - 2][x + 2] == '-') & (i - 1 != 0) & (i != 0):
                            ## jump over piece diagonally up right
                            tempState4[i][x], tempState4[i - 2][x + 2] = tempState4[i - 2][x + 2], tempState4[i][x]
                            tempState4[i - 1][x + 1] = '-'
                            result.append(toString(tempState4))
                    if tempState[i][-1] == 'b':
                        ## rightmost piece
                        if (tempState5[i - 1][-1] == '-') & (i != 0):
                            ## move diagonally up right
                            tempState5[i][-1], tempState5[i - 1][-1] = tempState5[i - 1][-1], tempState5[i][-1]
                            result.append(toString(tempState5))
                        elif (tempState5[i - 1][-1] == 'w') & (tempState5[i - 2][-1] == '-') & (i - 1 != 0) & (i != 0):
                            ## jump over piece diagonally up right
                            tempState5[i][-1], tempState5[i - 2][-1] = tempState5[i - 2][-1], tempState5[i][-1]
                            tempState5[i - 1][-1] = '-'
                            result.append(toString(tempState5))
                        if (tempState6[i - 1][-2] == '-') & (i != 0):
                            ## move diagonally up left
                            tempState6[i][-1], tempState6[i - 1][-2] = tempState6[i - 1][-2], tempState6[i][-1]
                            result.append(toString(tempState6))
                        elif (tempState6[i - 1][-2] == 'w') & (tempState6[i - 2][-3] == '-') & (i - 1 != 0) & (i != 0):
                            ## jump over piece diagonally up left
                            tempState6[i][-1], tempState6[i - 2][-3] = tempState6[i - 2][-3], tempState6[i][-1]
                            tempState6[i - 1][-2] = '-'
                            result.append(toString(tempState6))
                    if (i == 1) & (x == 1):
                        ## middle piece
                        if tempState13[i - 1][x] == '-':
                            ## move up diagonally left
                            tempState13[i][x], tempState13[i - 1][x] = tempState13[i - 1][x], tempState13[i][x]
                            result.append(toString(tempState13))
                        if tempState14[i - 1][x + 1] == '-':
                            ## move up diagonally right
                            tempState14[i][x], tempState14[i - 1][x + 1] = tempState14[i - 1][x + 1], tempState14[i][x]
                            result.append(toString(tempState14))
    return result


## whiteMove takes in the current board as an argument
## it returns a list of the possible white moves
## it iterates through the elements in the board and finds the Ws
## goes through if statements to check whether the W is on the top half of the board or the bottom half
## if its on the top half it does one set of moves
## if its on the bottom half it does another set of moves
## more if statements to check if the piece is on the leftmost or rightmost side of the row
## if it is it does one set of moves
## more if statements to check if the piece is in the middle of the row
## if it is it does another set of moves
## for every set of moves it can do, it creates a new board and appends it to a list
def whiteMove(board):
    result = []
    state = toArray(board)
    tempState = copy.deepcopy(state)
    tempState1 = copy.deepcopy(state)
    tempState2 = copy.deepcopy(state)
    tempState3 = copy.deepcopy(state)
    tempState4 = copy.deepcopy(state)
    tempState5 = copy.deepcopy(state)
    tempState6 = copy.deepcopy(state)
    tempState7 = copy.deepcopy(state)
    tempState8 = copy.deepcopy(state)
    tempState9 = copy.deepcopy(state)
    tempState10 = copy.deepcopy(state)
    tempState11 = copy.deepcopy(state)
    tempState12 = copy.deepcopy(state)
    tempState13 = copy.deepcopy(state)
    tempState14 = copy.deepcopy(state)
    n = sum(i.count('w') for i in state)
    numB = sum(i.count('w') for i in state)
    ## checks if player has no more pieces
    if (numB == 0):
        return board
    if (n == 0):
        return board
    firstRow = len(board[0])
    rows = (2 * firstRow) - 3
    middle = n - 2
    count = 0
    # print(tempState1)
    # state = toString(state)
    for i, j in enumerate(state):
        for x, y in enumerate(j):
            if y == 'w':
                if i == rows - 1:
                    count = count + 1
                ## checks if all the pieces are on the opponent's side
                if count == n:
                    return board
                if i < n - 2:
                    ## top half of board
                    if x == 0:
                        ## leftmost piece
                        if tempState1[i + 1][x] == '-':
                            ## move down one row
                            tempState1[i][x], tempState1[i + 1][x] = tempState1[i + 1][x], tempState1[i][x]
                            result.append(toString(tempState1))
                        elif (tempState1[i + 1][x] == 'b') & (tempState1[i + 2][x] == '-') & (i + 2 <= n - 2):
                            ## jump over piece down two rows
                            tempState1[i][x], tempState1[i + 2][x] = tempState1[i + 2][x], tempState1[i][x]
                            tempState1[i + 1][x] = '-'
                            result.append(toString(tempState1))
                        elif (tempState1[i + 1][x] == 'b') & (tempState1[i + 2][x + 1] == '-') & (i + 2 > n - 2):
                            ## jump over piece down two rows
                            tempState1[i][x], tempState1[i + 2][x + 1] = tempState1[i + 2][x + 1], tempState1[i][x]
                            tempState1[i + 1][x] = '-'
                            result.append(toString(tempState1))
                    if tempState[i][-1] == 'w':
                        ## rightmost piece
                        if tempState2[i + 1][-1] == '-':
                            ## move down one row
                            tempState2[i][-1], tempState2[i + 1][-1] = tempState2[i + 1][-1], tempState2[i][-1]
                            result.append(toString(tempState2))
                        elif (tempState2[i + 1][-1] == 'b') & (tempState2[i + 2][-1] == '-') & (i + 2 <= n - 2):
                            ## jump over piece down two rows
                            tempState2[i][-1], tempState2[i + 2][-1] = tempState2[i + 2][-1], tempState2[i][-1]
                            tempState2[i + 1][-1] = '-'
                            result.append(toString(tempState2))
                        elif (tempState2[i + 1][-1] == 'b') & (tempState2[i + 2][-2] == '-') & (i + 2 > n - 2):
                            ## jump over piece down two rows
                            tempState2[i][-1], tempState2[i + 2][-2] = tempState2[i + 2][-2], tempState2[i][-1]
                            tempState2[i + 1][-1] = '-'
                            result.append(toString(tempState2))
                    if (i == 0) & (x == 1):
                        ## second element middle piece in first row
                        if tempState7[i + 1][x - 1] == '-':
                            ## move down diagonally left
                            tempState7[i][x], tempState7[i + 1][x - 1] = tempState7[i + 1][x - 1], tempState7[i][x]
                            result.append(toString(tempState7))
                        if tempState8[i + 1][x] == '-':
                            ## move down diagonally right
                            tempState8[i][x], tempState8[i + 1][x] = tempState8[i + 1][x], tempState8[i][x]
                            result.append(toString(tempState8))
                        elif (tempState8[i + 1][x] == 'b') & (tempState8[i + 2][x] == '-'):
                            ## jump over piece diagonally down right
                            tempState8[i][x], tempState8[i + 2][x] = tempState8[i + 2][x], tempState8[i][x]
                            tempState8[i + 1][x] = '-'
                            result.append(toString(tempState8))
                    if (i == 0) & (x == 2):
                        ## third element middle piece in first row
                        if tempState9[i + 1][x - 1] == '-':
                            ## move down diagonally left
                            tempState9[i][x], tempState9[i + 1][x - 1] = tempState9[i + 1][x - 1], tempState9[i][x]
                            result.append(toString(tempState9))
                        elif (tempState9[i + 1][x - 1] == 'b') & (tempState9[i + 2][x - 2] == '-'):
                            ## jump over piece diagonally down left
                            tempState9[i][x], tempState9[i + 2][x - 2] = tempState9[i + 2][x - 2], tempState9[i][x]
                            tempState9[i + 1][x - 1] = '-'
                            result.append(toString(tempState9))
                        if tempState10[i + 1][x] == '-':
                            ## move down diagonally right
                            tempState10[i][x], tempState10[i + 1][x] = tempState10[i + 1][x], tempState10[i][x]
                            result.append(toString(tempState10))
                    if (i == 1) & (x == 1):
                        ## middle piece in second row
                        if tempState11[i + 1][x - 1] == '-':
                            ## move down diagonally left
                            tempState11[i][x], tempState11[i + 1][x - 1] = tempState11[i + 1][x - 1], tempState11[i][x]
                            result.append(toString(tempState11))
                        elif (tempState11[i + 1][x - 1] == 'b') & (tempState11[i + 2][x - 1] == '-'):
                            ## jump over piece diagonally down left
                            tempState11[i][x], tempState11[i + 2][x - 1] = tempState11[i + 2][x - 1], tempState11[i][x]
                            tempState11[i + 1][x - 1] = '-'
                            result.append(toString(tempState11))
                        if tempState12[i - 1][x] == '-':
                            ## move down diagonally right
                            tempState12[i][x], tempState12[i + 1][x] = tempState12[i + 1][x], tempState12[i][x]
                            result.append(toString(tempState12))
                        elif (tempState12[i + 1][x] == 'b') & (tempState12[i + 2][x + 1] == '-'):
                            ## jump over piece diagonally down right
                            tempState12[i][x], tempState12[i + 2][x + 1] = tempState12[i + 2][x + 1], tempState12[i][x]
                            tempState12[i + 1][x] = '-'
                            result.append(toString(tempState12))

                if (i >= n - 2) & ( i != rows - 1) :
                    ## bottom half of board
                    if x == 0:
                        ## leftmost piece
                        if tempState3[i + 1][x] == '-':
                            ## move diagonally down left
                            tempState3[i][x], tempState3[i + 1][x] = tempState3[i + 1][x], tempState3[i][x]
                            result.append(toString(tempState3))
                        elif (i + 1 != rows - 1) & (i != rows - 1):
                            if (tempState3[i + 1][x] == 'b') & (tempState3[i + 2][x] == '-'):
                                ## jump over piece diagonally down left
                                tempState3[i][x], tempState3[i + 2][x] = tempState3[i + 2][x], tempState3[i][x]
                                tempState3[i + 1][x] = '-'
                                result.append(toString(tempState3))
                        if tempState4[i + 1][x + 1] == '-':
                            ## move diagonally down right
                            tempState4[i][x], tempState4[i + 1][x + 1] = tempState4[i + 1][x + 1], tempState4[i][x]
                            result.append(toString(tempState4))
                        elif (i + 1 != rows - 1) & (i != rows - 1):
                            if (tempState4[i + 1][x + 1] == 'b') & (tempState4[i + 2][x + 2] == '-'):
                                ## jump over piece diagonally down right
                                tempState4[i][x], tempState4[i + 2][x + 2] = tempState4[i + 2][x + 2], tempState4[i][x]
                                tempState4[i + 1][x + 1] = '-'
                                result.append(toString(tempState4))
                    if tempState[i][-1] == 'w':
                        ## rightmost piece
                        if tempState5[i + 1][-1] == '-':
                            ## move diagonally down right
                            tempState5[i][-1], tempState5[i + 1][-1] = tempState5[i + 1][-1], tempState5[i][-1]
                            result.append(toString(tempState5))
                        elif (i + 1 != rows - 1) & (i != rows - 1):
                            if (tempState5[i + 1][-1] == 'b') & (tempState5[i + 2][-1] == '-'):
                                ## jump over piece diagonally down right
                                tempState5[i][-1], tempState5[i + 2][-1] = tempState5[i + 2][-1], tempState5[i][-1]
                                tempState5[i + 1][-1] = '-'
                                result.append(toString(tempState5))
                        if tempState6[i + 1][-2] == '-':
                            ## move diagonally down left
                            tempState6[i][-1], tempState6[i + 1][-2] = tempState6[i + 1][-2], tempState6[i][-1]
                            result.append(toString(tempState6))
                        elif (i + 1 != rows - 1) & (i !=  rows - 1):
                            if (tempState6[i + 1][-2] == 'b') & (tempState6[i + 2][-3] == '-'):
                                ## jump over piece diagonally down left
                                tempState6[i][-1], tempState6[i + 2][-3] = tempState6[i + 2][-3], tempState6[i][-1]
                                tempState6[i + 1][-2] = '-'
                                result.append(toString(tempState6))
                    if (i == rows - 2) & (x == 1):
                        ## middle piece
                        if tempState13[i + 1][x] == '-':
                            ## move down diagonally left
                            tempState13[i][x], tempState13[i + 1][x] = tempState13[i + 1][x], tempState13[i][x]
                            result.append(toString(tempState13))
                        if tempState14[i + 1][x + 1] == '-':
                            ## move down diagonally right
                            tempState14[i][x], tempState14[i + 1][x + 1] = tempState14[i + 1][x + 1], tempState14[i][x]
                            result.append(toString(tempState14))
    return result


## changes representation of the board to a 2D array
def toArray(lst):
    result = []
    for char in lst:
        result.append(list(char))
    return result

## changes representation of the board back to its original form
def toString(lst):
    result = []
    for char in lst:
        result.append(''.join(char))
    return result
    
