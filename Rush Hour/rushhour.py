## rushhour.py
## Maayez Imam 915342727

import numpy as np
import copy
from queue import PriorityQueue
from queue import Queue

# class for the cars, their coordinates on the board,
# their placement on the board (horizontal, vertical)
# and character of the car
# DID NOT END UP USING
class Car:
    def __init__(self, coordinate, placement, character):
        self.coordinate = coordinate
        self.placement = placement
        self.character = character

# class for the puzzle, its matrix and the cars on it
# DID NOT END UP USING
class Puzzle:
    def __init__(self, matrix, cars):
        self.matrix = matrix
        self.cars = cars

# check value of heuristic parameter and pass initial state to corresponding function
# checks to see if incorrect value of heuristic was entered
# also checks for edge case for when board is in goal state initially
# prints out solution after running through heuristic and A* algorithm
def rushhour(heuristic, initial):
    result = []
    if goalCheck(initial) == True:
        return printSolution(initial)

    # change representation of state to make it easier for me
    newInit = toArray(initial)

    if heuristic == 0:
        # use blocking heuristic
        result = blocking(newInit)
        return printSolution(result)
    elif heuristic == 1:
        # use my own heuristic
        result = unique(newInit)
        return printSolution(result)
    else:
        print("incorrect heuristic input")

# function to print the solution in the desired format
# changes the 2d array back to its 1d format
# enumerates through the resulting list and prints out each one
# calculates moves by calculating how many elements in the final list
# did not figure out how to calculate states so just left it the same as moves for now
def printSolution(result):
    result = toString(result)
    # print(result)
    moves = 0
    states = 0
    for j, d in enumerate(result):
        print(d)
    for j, d in enumerate(result):
        moves = int((len(result) / 6) - 1)
        states = int((len(result) / 6) - 1)
    print("Total moves: ", moves)
    print("Total states explored: ", states)


# generate h(n) value for each state and pass it to a* function for it to generate new states
# counts the number of cars blocking the X car from the goal state
def blocking(state):
    frontier = []
    count = 0
    block = []

    for i, j in enumerate(state):
        if (j[i] != 'X') & (j[i] != '-'):
            count = count + 1
    block.append(count)

    for lst in state:
        frontier.append(lst)
    # frontier.sort()
    result = astar(state, frontier)
    return result

# my unique heuristic
# incomplete
def unique(state):
    frontier = []
    for lst in state:
        frontier.append(lst)
    result = astar(state, frontier)
    return result

# the A* algorithm that takes in the sorted frontier, pops the first element from it
# and checks if it is the goal state. If not, it expands it by generating new nodes
# and puts those nodes onto the frontier and sorts them again
def astar(state, frontier):
    if frontier == []:
        return []

    for i, c in enumerate(frontier[0:6]):
        if 'X' in c[5]:
            # chosen node matches goal node
            return state
        else:
            # expand chosen node to get new nodes
            # generateNewStates?
            generateNewStates(frontier[0:6])

    return state
    # call blocking(frontier) again

# check if car can move up
def validUp(state):
    return 0

# operator to move the car up
# goes through each element in the list and if an index matches a
# coordinate from the isVertical function, it swaps it with the
# element above it
def moveUp(state):
    result = []
    tempState = copy.deepcopy(state)
    coordinates = isVertical(tempState)

    if 0 in coordinates[0]:
        return state

    for i, lst in enumerate(state):
        for j, letter in enumerate(lst):
            if letter == coordinates[i][j]:
                tempState[i][j], tempState[i - 1][j] = tempState[i - 1][j], tempState[i][j]
                result.append(tempState)

    return result

# check if car can move down
def validDown(state):
    return 0

# operator to move the car down
# goes through each element in the list and if an index matches a
# coordinate from the isVertical function, it swaps it with the
# element below it
def moveDown(state):
    result = []
    tempState = copy.deepcopy(state)
    coordinates = isVertical(tempState)

    if 5 in coordinates[0]:
        return state

    for i, lst in enumerate(state):
        for j, letter in enumerate(lst):
            if letter == coordinates[i][j]:
                print("in if")
                tempState[i][j], tempState[i + 1][j] = tempState[i + 1][j], tempState[i][j]
                result.append(tempState)

    return result


# check if car can move right
def validRight(state):
    return 0

# operator to move the car right
# goes through each element in the list and if an index matches a
# coordinate from the isHorizontal function, it swaps it with the
# element to the right of it
def moveRight(state):
    result = []
    tempState = copy.deepcopy(state)
    coordinates = isHorizontal(tempState)

    if 5 in coordinates[1]:
        return state
    # print(coordinates)

    for i, lst in enumerate(coordinates):
        for j, letter in enumerate(lst):
            if letter == coordinates:
                print("in if")
                tempState[i][j], tempState[i][j + 1] = tempState[i][j + 1], tempState[i][j]
                result.append(tempState)

    return result


# check if car can move left
def validLeft():
    return 0

# operator to move the car left
# goes through each element in the list and if an index matches a
# coordinate from the isHorizontal function, it swaps it with the
# element to the left of it
def moveLeft(state):
    result = []
    tempState = copy.deepcopy(state)
    coordinates = isHorizontal(tempState)

    if 0 in coordinates[1]:
        return state
    # print(coordinates)

    for i, lst in enumerate(coordinates):
        for j, letter in enumerate(lst):
            if letter == coordinates:
                print("in if")
                tempState[i][j], tempState[i][j - 1] = tempState[i][j - 1], tempState[i][j]
                result.append(tempState)

    return result


# function to generate new states based on the moves the cars can make
# at a given time
def generateNewStates(state):
    # return moveUp(state) + moveDown(state) + moveRight(state) + moveLeft(state)
    return 0


# finds the coordinates of the vertical cars
# enumerates through the state, finds anything that isn't an '-' or 'X'
# checks if it has something above or below it
# adds the coordinate to a list to use in moveUp and moveDown
def isVertical(state):
    coordinates = []
    for i, lst in enumerate(state):
        for j, letter in enumerate(lst):
            if (letter != '-') & (letter != 'X'):
                if (state[i][j] == state[i-1][j]) or (state[i][j] == state[i+1][j]):
                    coordinates.append([i, j])
    return coordinates
    # might have to check for cars of different letters and differentiating them from each other


# finds the coordinates of the horizontal cars
# enumerates through the state, finds anything that isn't an '-' or 'X'
# checks if it has something to the right or to the left of it
# adds the coordinate to a list to use in moveRight and moveLeft
def isHorizontal(state):
    coordinates = []
    for i, lst in enumerate(state):
        for j, letter in enumerate(lst):
            if (letter != '-') & (letter != 'X'):
                if (state[i][j] == state[i][j+1]) or (state[i][j] == state[i][j-1]):
                    coordinates.append([i, j])
    return coordinates
    # might have to check for cars of different letters and differentiating them from each other


# checks to see if the X car is in the goal state or not, returns True if it is and False if not
def goalCheck(state):
    for i, c in enumerate(state):
        if 'X' in c[5]:
            return True
        else:
            return False

# changes representation of the board to a 2D array
def toArray(lst):
    result = []
    for char in lst:
        result.append(list(char))
    return result

# changes representation of the board back to its original form
def toString(lst):
    result = []
    for char in lst:
        result.append(''.join(char))
    return result
  
  
