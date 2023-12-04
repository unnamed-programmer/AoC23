import os
import math
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

scratchCard = {}

for line in inputArray:
    thingNumber    = int(line.split(':')[0].split(' ')[-1])
    line           = line.split(':')[1].strip('\n')
    winningNumbers = [int(i) for i in line.split('|')[0].split(' ') if i != '']
    chosenNumbers  = [int(i) for i in line.split('|')[1].split(' ') if i != '']
    scratchCard[thingNumber] = (winningNumbers, chosenNumbers, 1)

# parse inputs to get lists of winning and chosen numbers
for index in scratchCard:
    winningNumbers, chosenNumbers, timesToRun = scratchCard[index]
    print(f"{winningNumbers} | {chosenNumbers}, run {timesToRun} time(s)")

    # find winning numbers
    cardWins = 0
    for chosenNumber in chosenNumbers:
        if chosenNumber in winningNumbers:
            cardWins += 1
            print(f"{chosenNumber} yes it's in, score is now {cardWins}")
        else:
            print(f"{chosenNumber} ISN'T, score is now {cardWins}")
    print(cardWins)

    for i in range(1, cardWins + 1):
        scratchCard[index + i] = (scratchCard[index + i][0], scratchCard[index + i][1], scratchCard[index + i][2] + timesToRun)

totalScore = 0


for index in scratchCard:
    _, _, timesToRun = scratchCard[index]
    totalScore += timesToRun
    print("Score is ", totalScore)

print(totalScore)