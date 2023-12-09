import os
def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
sequenceRanges = [[[int(i) for i in line.strip().split(' ')]] for line in inputArray]

# Find change patterns in each sequence and add to the lists
for sequenceRange in sequenceRanges:
    proceeding = True
    sequenceIndex = 0
    while proceeding:
        if all(sequenceRange[sequenceIndex][i] == 0 for i in range(len(sequenceRange[sequenceIndex]))):
            proceeding = False
            break
        sequenceRange.append([])
        for index in range(len(sequenceRange[sequenceIndex]) - 1):
            number = sequenceRange[sequenceIndex][index]
            nextNumber = sequenceRange[sequenceIndex][index + 1]
            sequenceRange[sequenceIndex + 1].append(nextNumber - number)
        sequenceIndex += 1

# Extrapolate next value of each sequence
extrapolatedValuesSum = 0
for sequenceRange in sequenceRanges:
    for sequenceIndex in range(len(sequenceRange) - 1, -1, -1):
        sequence = sequenceRange[sequenceIndex]
        if all(i == 0 for i in sequence):
            sequence.insert(0, 0)
        else:
            extrapolatedValue = sequence[0] - sequenceRange[sequenceIndex + 1][0]
            if sequenceIndex == 0:
                extrapolatedValuesSum += extrapolatedValue
            sequence.insert(0, extrapolatedValue)

print(extrapolatedValuesSum)