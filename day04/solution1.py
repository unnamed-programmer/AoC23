import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "testin.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

totalScore = 0

for scratchCard in inputArray:
    # parse inputs to get lists of winning and chosen numbers
    scratchCard = scratchCard.split(':')[1].strip('\n')
    winningNumbers = scratchCard.split('|')[0].split(' ')
    chosenNumbers = scratchCard.split('|')[1].split(' ')
    for i, j in enumerate(winningNumbers):
        if j == '': winningNumbers.pop(i)
    for i, j in enumerate(chosenNumbers):
        if j == '': chosenNumbers.pop(i)
    print(f"{winningNumbers} | {chosenNumbers}")

    # find winning numbers
    cardWins = 0
    for winningNumber in winningNumbers:
        if winningNumber in chosenNumbers:
            if cardWins == 0:
                cardWins = 1
            else:
                cardWins *= 2
            print(f"{winningNumber} in {chosenNumbers}, score is now {cardWins}")

    totalScore += cardWins
    print(f"Total score is {totalScore}")

print(totalScore)