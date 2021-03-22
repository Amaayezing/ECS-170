## tilepuzzle.py
## Maayez Imam 915342727

import copy
import sys

def tilepuzzle(start, goal):
    return reverse(statesearch([start], goal, []))


def statesearch(unexplored, goal, path):
    sys.setrecursionlimit(100000)
    # print(path)
    # print("path")
    # print(path)
    # print("unexplored")
    # print(unexplored)
    # print("head unexplored")
    # print(head(unexplored))
    if unexplored == []:
        # print("unexplored == []")
        return []
    elif goal == head(unexplored):
        # print("goal == head unexplored")
        return cons(goal, path)
    elif len(path) == 100:
        return statesearch(tail(unexplored), goal, path)
    elif head(unexplored) in path:
        # print("head unexplored in path")
        unexplored.remove(head(unexplored))
        # print(path)
        # print(unexplore
        return statesearch(unexplored, goal, path)
        # test for cycles here (if the head of the unexplored (currState) is already in the path):
        # do something appropriate here
    else:
        # print("result")
        # print(result)
        result = statesearch(generateNewStates(head(unexplored)),
                         goal,
                         cons(head(unexplored), path))

        # print("result")
        # print(result)
        if result != []:
            # print("result != []")
            return result
        else:
            # print("tail unexplored search")
            return statesearch(tail(unexplored),
                               goal,
                               path)


def moveRight(currState):
    # check if valid move
    result = []
    tempState = copy.deepcopy(currState)

    for sublist in currState:
        if sublist[2] == 0:
            return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i][j+1] = tempState[i][j+1], tempState[i][j]
                result.append(tempState)

    return result

def moveLeft(currState):
    # check if valid move
    result = []
    tempState = copy.deepcopy(currState)

    for sublist in currState:
        if sublist[0] == 0:
            return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i][j - 1] = tempState[i][j - 1], tempState[i][j]
                result.append(tempState)

    return result

def moveUp(currState):
    # check if valid move
    result  = []
    tempState = copy.deepcopy(currState)

    if 0 in currState[0]:
        return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i - 1][j] = tempState[i - 1][j], tempState[i][j]
                result.append(tempState)

    return result

def moveDown(currState):
    # check if valid move
    result = []
    tempState = copy.deepcopy(currState)

    if 0 in currState[2]:
        return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i + 1][j] = tempState[i + 1][j], tempState[i][j]
                result.append(tempState)

    return result

def reverseEach(listOfLists):
    result = []
    for st in listOfLists:
        result.append(reverse(st))
    return result

def reverse(st):
    return st[::-1]


def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def take(n, lst):
    return lst[0:n]


def drop(n, lst):
    return lst[n:]


def cons(item, lst):
    return [item] + lst


def generateNewStates(currState):
    return (moveUp(currState) + moveDown(currState) +
            moveRight(currState) + moveLeft(currState))
