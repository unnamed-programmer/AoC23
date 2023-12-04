# put the input into inputArray, not strictly necessary but makes life easier
import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")
with open(filename, 'r') as f:
    inputArray = f.readlines()

# parse inputs and convert to a single scratchCard dictionary
scratchCard = {}
for line in inputArray:
    thingNumber    = int(line.split(':')[0].split(' ')[-1])
    line           = line.split(':')[1].strip('\n')
    winningNumbers = [int(i) for i in line.split('|')[0].split(' ') if i != '']
    chosenNumbers  = [int(i) for i in line.split('|')[1].split(' ') if i != '']
    scratchCard[thingNumber] = (winningNumbers, chosenNumbers, 1)

# unpack each item in scratchCard dict, find number of matches
# then increment the timesToRun of subsequent cards by the timesToRun of the current card
for index in scratchCard:
    winningNumbers, chosenNumbers, timesToRun = scratchCard[index]
    cardWins = sum(int(chosenNumber in winningNumbers) for chosenNumber in chosenNumbers)
    for i in range(1, cardWins + 1):
        scratchCard[index + i] =  (scratchCard[index + i][0], scratchCard[index + i][1], scratchCard[index + i][2] + timesToRun)

# add up all timesToRun values of the scratchcards
totalScore = sum(scratchCard[index][2] for index in scratchCard)
print(totalScore)