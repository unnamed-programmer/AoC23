import os
def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

import itertools
inputArray = [i.strip() for i in getInput()]
width = len(inputArray[0])
height = len(inputArray)

emptyRows = [i for i in range(width)  if all(inputArray[i][j] == '.' for j in range(height))][::-1]
emptyCols = [i for i in range(height) if all(inputArray[j][i] == '.' for j in range(width) )][::-1]

for col in emptyCols:
    inputArray = [''.join([i[:col], '!', i[col + 1:]]) for i in inputArray]
width = len(inputArray[0])
for row in emptyRows:
    inputArray.pop(row)
    inputArray.insert(row, '!' * width)
height = len(inputArray)

galaxies = [(x, y)
            for y, x in itertools.product(range(height), range(width))
            if inputArray[y][x] == '#']

galaxyPairs = list(itertools.combinations(galaxies, 2))

distanceSum = 0
for pair in galaxyPairs:
    distance = 0
    lowestX = min(pair[0][0], pair[1][0])
    lowestY = min(pair[0][1], pair[1][1])
    highestX = max(pair[0][0], pair[1][0])
    highestY = max(pair[0][1], pair[1][1])
    x, y = lowestX, lowestY
    while x != highestX:
        x += 1
        distance += 1000000 if inputArray[y][x] == '!' else 1
        # print(distance)
    while y != highestY:
        y += 1
        distance += 1000000 if inputArray[y][x] == '!' else 1
        # print(distance)
    distanceSum += distance

print('dingus')
print(distanceSum)

# it's above 82000292