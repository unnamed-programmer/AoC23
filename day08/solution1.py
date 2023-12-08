import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")
with open(filename, 'r') as f:
    inputArray = f.readlines()
directions = inputArray[0].strip()

for i in range(2, len(inputArray)):
    line = inputArray[i]
    instruction = line.split('=')[0].strip()
    definition = line.split('=')[1].strip()