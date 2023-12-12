import os

def findMiddlePoint(directions: tuple[bool]):
    pass

def getConnections(point: tuple[int]):
    connectsLft = inputArray[startIndex[0]][startIndex[1] - 1] in ['-', 'L', 'F']
    connectsRgt = inputArray[startIndex[0]][startIndex[1] + 1] in ['-', 'J', '7']
    connectsTop = inputArray[startIndex[0] - 1][startIndex[1]] in ['|', '7', 'F']
    connectsBtm = inputArray[startIndex[0] + 1][startIndex[1]] in ['|', 'L', 'J']
    return (connectsLft, connectsRgt, connectsTop, connectsBtm)

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "testin.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

import itertools
inputArray = getInput()

for y, x in itertools.product(range(len(inputArray)), range(len(inputArray[0]))):
    if inputArray[y][x] == 'S':
        startIndex = (x, y)
        break

startConnections = getConnections(startIndex) # type: ignore
