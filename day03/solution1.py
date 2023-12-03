import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "testin.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

# Find the possible symbols in the file (could be hardcoded but nah)
known_chars = set('.0123456789\n')
possibleSymbols = set()
for row in inputArray:
    possibleSymbols.update(set(row) - known_chars - possibleSymbols)
possibleSymbols = list(possibleSymbols)
print(possibleSymbols)

# Find indices of each symbol
indices = []
for i, row in enumerate(inputArray):
    indices.extend((i, j) for j, symbol in enumerate(row) if symbol in possibleSymbols)

# Calculate adjacent numbers
partNumbers = []

for index in indices:
    partNumber = []
    adjacentIndices = [(int(index[0] + i), int(index[1] + j)) for i in (-1, 0, 1) for j in (-1, 0, 1)]
    for adjacentIndex in adjacentIndices:
        if inputArray[adjacentIndex[0]][adjacentIndex[1]].isdigit():
            partNumber.insert(0, inputArray[adjacentIndex[0]][adjacentIndex[1]])
            i = 1
            while inputArray[adjacentIndex[0]][adjacentIndex[1] - i].isdigit():
                partNumber.insert(0, inputArray[adjacentIndex[0]][adjacentIndex[1] - i])
                i += 1
            i = 1
            while inputArray[adjacentIndex[0]][adjacentIndex[1] + i].isdigit():
                partNumber.insert(-1, inputArray[adjacentIndex[0]][adjacentIndex[1] - i])
                i += 1
        partNumber = "".join(partNumber)
        partNumbers.append(partNumber)
        print(partNumbers)





# Add up numbers to find total
