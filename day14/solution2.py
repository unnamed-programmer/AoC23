import os

def generateArray():
    global roundedRocks
    global staticRocks
    global width
    global height
    array = [['.' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if [x, y] in staticRocks:
                array[y][x] = '#'
            if any([x, y] in roundedRock for roundedRock in roundedRocks):
                array[y][x] = 'O'
    for i in array: print(i)
    print()

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "testin.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
inputArray = [list(y.strip()) for y in inputArray]

roundedRocks = []
staticRocks = []
height = len(inputArray)
width = len(inputArray[0])

for y in range(len(inputArray)):
    for x in range(len(inputArray[y])):
        if inputArray[y][x] == 'O':
            roundedRocks.append([[x, y], 4])
        if inputArray[y][x] == '#':
            staticRocks.append([x, y])

generateArray()
dingus = []
for roundedRock in roundedRocks:
    dingus.append(roundedRock)

for _ in range(1000000000):
    print(f'\n{_ + 1} of 1000000000')


    # North
    move = True
    while move:
        move = False
        for rock in roundedRocks:
            if (
                # rock[1] > 0
                rock[0][1] != 0
                and [rock[0][0], rock[0][1] - 1] not in staticRocks
                and all(
                    [rock[0][0], rock[0][1] - 1] != roundedRock[0]
                    for roundedRock in roundedRocks
                )
            ):
                rock[0][1] -= 1
                rock[1] = 4
                move = True
            else:
                rock[1] -= 1
    generateArray()

    # West
    move = True
    while move:
        move = False
        for rock in roundedRocks:
            if (
                # rock[1] > 0
                rock[0][0] != 0
                and [rock[0][0] - 1, rock[0][1]] not in staticRocks
                and all(
                    [rock[0][0] - 1, rock[0][1]] != roundedRock[0]
                    for roundedRock in roundedRocks
                )
            ):
                rock[0][0] -= 1
                rock[1] = 4
                move = True
            else:
                rock[1] -= 1
    generateArray()

    # South
    move = True
    while move:
        move = False
        for rock in roundedRocks:
            if (
                # rock[1] > 0
                rock[0][1] != height - 1
                and [rock[0][0], rock[0][1] + 1] not in staticRocks
                and all(
                    [rock[0][0], rock[0][1] + 1] != roundedRock[0]
                    for roundedRock in roundedRocks
                )
            ):
                rock[0][1] += 1
                rock[1] = 4
                move = True
            else:
                rock[1] -= 1
    generateArray()

    # East
    move = True
    while move:
        move = False
        for rock in roundedRocks:
            if (
                # rock[1] > 0
                rock[0][0] != width - 1
                and [rock[0][0] + 1, rock[0][1]] not in staticRocks
                and all(
                    [rock[0][0] + 1, rock[0][1]] != roundedRock[0]
                    for roundedRock in roundedRocks
                )
            ):
                rock[0][0] += 1
                rock[1] = 4
                move = True
            else:
                rock[1] -= 1
    generateArray()

    # if all(rock[1] == 0 for rock in roundedRocks): break
    if all(roundedRocks[i][0] == previousRoundedRocks[i][0] for i in range(len(roundedRocks))):
        break

loadTotal = 0

for y in range(len(inputArray)):
    for x in range(len(inputArray[y])):
        if inputArray[y][x] == 'O':
            loadTotal += height - y

print(loadTotal)