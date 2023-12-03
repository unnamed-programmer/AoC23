import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "testin.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

possibleSymbols = []

for row in inputArray:
    for char in row:
        if char not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n'] and char not in possibleSymbols:
            possibleSymbols.append(char)

print(possibleSymbols)