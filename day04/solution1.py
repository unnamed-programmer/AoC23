import os
import math
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

totalScore = 0

for scratchCard in inputArray:
    # parse inputs to get lists of winning and chosen numbers
    if scratchCard == "Card   3:  4 45 78 42 29 92 16 90 93 30 | 97 90 75 40 43 65 92 83 41  4 47 35 29 80 68 87 30 71 98 42 95  7 76 69 88\n":
        pass
    scratchCard = scratchCard.split(':')[1].strip('\n')
    winningNumbers = scratchCard.split('|')[0].split(' ')
    chosenNumbers = scratchCard.split('|')[1].split(' ')
    winningNumbers = [i for i in winningNumbers if i != '']
    chosenNumbers = [i for i in chosenNumbers if i != '']
    for helpMe in chosenNumbers:
        if helpMe == '':
            raise RuntimeError("AAAAAAAAAAAAAAA ", chosenNumbers)
    for helpMe in winningNumbers:
        if helpMe == '':
            raise RuntimeError("AAAAAAAAAAAAAAA ", winningNumbers)

    chosenNumbers = [int(k) for k in chosenNumbers]
    winningNumbers = [int(k) for k in winningNumbers]

    print(f"{winningNumbers} | {chosenNumbers}")

    print(bool(set(chosenNumbers).intersection(set(winningNumbers))))

    # find winning numbers
    print(f"Winning: {winningNumbers}")
    cardWins = 0
    for chosenNumber in chosenNumbers:
        if chosenNumber in winningNumbers:
            cardWins += 1
            print(f"{chosenNumber} yes it's in, score is now {cardWins}")
        else:
            print(f"{chosenNumber} ISN'T, score is now {cardWins}")

    if bool(cardWins) != bool(set(chosenNumbers).intersection(set(winningNumbers))):
        raise RuntimeError("FUCK")

    totalScore += math.floor(2 ** (cardWins - 1))
    print(f"Total score is {totalScore}")

if totalScore == 17790:
    raise RuntimeError("FUCK") # it's below 17790
print(totalScore)