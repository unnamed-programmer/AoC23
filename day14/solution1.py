import os

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
inputArray = [list(y.strip()) for y in inputArray]

# Shift the Os up to the top point
anyMove = True
while anyMove:
    anyMove = False
    for y in range(len(inputArray)):
        print(f'y {y}')
        for x in range(len(inputArray[y])):
            if inputArray[y][x] == 'O' and inputArray[y - 1][x] == '.' and y != 0:
                inputArray[y - 1][x] = 'O'
                inputArray[y][x] = '.'
                anyMove = True

height = len(inputArray)
loadTotal = 0

for y in range(len(inputArray)):
    for x in range(len(inputArray[y])):
        if inputArray[y][x] == 'O':
            loadTotal += height - y

print(loadTotal)