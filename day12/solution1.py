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

for row in inputArray:
    allRowCombinations = []
    sequence = row[0]
    runLengths = row[1]
    length = len(sequence)
    gapsTotal = length - sum(runLengths)
    spaces = [0 for _ in range(len(runLengths) - 1)]
    if gapsTotal - len(spaces) > 0:
        gapCombinations = []
        for offset in range(gapsTotal - len(spaces) + 1):
            gapCombinations += [insertReturn(i, 0, offset) for i in splitNumber(gapsTotal - offset, len(spaces))]
    else:
        gapCombinations = splitNumber(gapsTotal, len(spaces))

    # Find all possible combinations
    for gapCombination in gapCombinations:
        listToAppend = ''
        for i in range(len(runLengths)):
            if len(gapCombination) == len(runLengths):
                for _ in range(gapCombination[i]):
                    listToAppend += '.'
            for _ in range(runLengths[i]):
                listToAppend += '#'
            if len(gapCombination) != len(runLengths) and i < len(gapCombination):
                for _ in range(gapCombination[i]):
                    listToAppend += '.'
        allRowCombinations.append(listToAppend)

    # Eliminate all combinations that don't work
    possibleRowCombinations = []
    for rowCombination in allRowCombinations:
        rowPossible = True
        for i in range(len(rowCombination)):
            if sequence[i] != '?' and sequence[i] != rowCombination[i]:
                rowPossible = False
        if rowPossible:
            possibleRowCombinations.append(rowCombination)

    print('e')




# PLAN
# generate possible combinations using RLE and the length
# compare to the sequence and eliminate ones that don't work

# NB runLengths are the broken ones