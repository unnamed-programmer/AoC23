import itertools
import os

def insertReturn(lst: list, index: int, value):
    lst.insert(index, value)
    return lst

def splitNumber(number, parts):
    if parts == 1:
        return [[number]]
    else:
        result = []
        for i in range(1, number):
            for combination in splitNumber(number - i, parts - 1):
                result.append([i] + combination)
        return result

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "testin.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = [[i.strip('\n').split(' ')[0], [int(j) for j in i.strip('\n').split(' ')[1].split(',')]] for i in getInput()]
totalPossible = 0

for row in inputArray:
    allRowCombinations = []
    sequence = row[0]
    runLengths = row[1]
    length = len(sequence)
    gapsTotal = length - sum(runLengths)
    spaces = [0 for _ in range(len(runLengths) - 1)]
    if gapsTotal - len(spaces) > 0:
        gapCombinations = []
        for preOffset in range(gapsTotal - len(spaces) + 1):
            for postOffset in range(gapsTotal - len(spaces) - preOffset + 1):
                gapCombinations += [[preOffset] + splitNum + [postOffset] for splitNum in splitNumber(gapsTotal - preOffset - postOffset, len(spaces))]
    else:
        gapCombinations = [[0] + splitNum + [0] for splitNum in splitNumber(gapsTotal, len(spaces))]


    # Find all possible combinations
    for gapCombination in gapCombinations:
        listToAppend = ''

        for _ in range(gapCombination[0]):
            listToAppend += '.'

        for indexRL in range(len(runLengths)):

            for _ in range(runLengths[indexRL]):
                listToAppend += '#'

            if indexRL < len(runLengths):
                for _ in range(gapCombination[indexRL + 1]):
                    listToAppend += '.'

        allRowCombinations.append(listToAppend)

    # Eliminate all combinations that don't work
    possibleRowCombinations = []
    for rowCombination in allRowCombinations:
        rowPossible = all(
            sequence[indexRC] in ['?', rowCombination[indexRC]]
            for indexRC in range(len(rowCombination))
        )
        if rowPossible:
            possibleRowCombinations.append(rowCombination)
        print(f'{rowCombination} is {'GOOD' if rowPossible else 'bad'}')

    totalPossible += len(possibleRowCombinations)

    print(totalPossible)




# PLAN
# generate possible combinations using RLE and the length
# compare to the sequence and eliminate ones that don't work

# NB runLengths are the broken ones