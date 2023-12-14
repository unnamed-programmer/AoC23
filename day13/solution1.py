import os

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "testin.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()

inputArray = [_.strip() for _ in inputArray]
proceed = True
startIndex = 0
while proceed:
    thisArray = []
    for lIndex in range(startIndex, len(inputArray)):
        line = inputArray[lIndex]
        if line == '': startIndex = lIndex + 1; break
        thisArray.append(line)

    for i in range(len(thisArray) - 1):
        if thisArray[i] == thisArray[i + 1]:
            mirrorTop = i
            mirrorBtm = i + 1

    for i in range(len(thisArray[0]) - 1):
        if [_[i] for _ in thisArray] == [_[i + 1] for _ in thisArray]:
            mirrorLft = i
            mirrorRgt = i + 1

    if lIndex + 1 == len(inputArray): proceed = False
