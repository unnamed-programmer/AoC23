import os

def hashString(s: str) -> int:
    hashVal = 0
    for char in s:
        hashVal += ord(char)
        hashVal *= 17
        hashVal %= 256
    return hashVal

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
inputArray = inputArray[0].strip('\n').split(',')

hashTotal = 0
for step in inputArray:
    hashTotal += hashString(step)

print(hashTotal)