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

answer = next(iter(elementMap))
steps = 0

while answer != 'ZZZ':
    for side in directions:
        element = elementMap[answer]
        answer = element[0] if side == 'L' else element[1]
        steps += 1
        print(f'{steps} - {answer}: {elementMap[answer]}, {side}')
        # if 'ZZZ' in elementMap[answer][0]: raise RuntimeError('dingus')
        if answer == 'ZZZ':
            break
        if steps >= 100000: raise RuntimeError('nah too high')


# between 10000 and 100000
# print(steps)