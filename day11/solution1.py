import os
def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = [i.strip() for i in getInput()]
width = len(inputArray[0])
height = len(inputArray)

emptyRows = [i for i in range(width)  if all(inputArray[i][j] == '.' for j in range(height))][::-1]
emptyCols = [i for i in range(height) if all(inputArray[j][i] == '.' for j in range(width))][::-1]

for col in emptyCols:
    inputArray = [f'{i[:col]}.{i[col:]}' for i in inputArray]
width = len(inputArray[0])
for row in emptyRows:
    inputArray.insert(row, '.' * width)


print('dingus')