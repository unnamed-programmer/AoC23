import os

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
directions = inputArray[0].strip()

def findElementMap(inputArray):
    elementMap = {}
    for i in range(2, len(inputArray)):
        line = inputArray[i]
        instruction = line.split('=')[0].strip()
        definition = line.split('=')[1].strip()
        definition = "".join(char for char in definition if char not in "() ").split(',')
        elementMap[instruction] = definition
    return elementMap

elementMap = findElementMap(inputArray)
firstMap = next(iter(elementMap))


answer = 'AAA'
continuing = True
tries = 0

while continuing:
    for direction in directions:
        element = elementMap[answer]
        answer = element[0] if direction == 'L' else element[1]
        if answer == 'ZZZ': continuing = False
        tries += 1
        print(answer)
        if tries >= 100000: raise RuntimeError

print(tries)