def findMostCommon(card: list[int | str]) -> int:
    for i in card:
        if isinstance(i, str):
            card.remove(i)
    if not card: card = [1]
    mostCommon = max(card, key=card.count)
# sourcery skip: swap-if-expression
    return mostCommon if not isinstance(mostCommon, str) else 1

def gradeCard(card: list[int | str]) -> int:
    # return (grade, digit0, digit1..4) in int form, g01234
    mostCommon = findMostCommon(card)
    card = [mostCommon if i == 'J' else i for i in cards]
    maxFrequency = card.count(mostCommon)
    cardCopy = [c for c in card if c != mostCommon]
    result = ''
    match maxFrequency:
        case 5:
            result = '7'
        case 4:
            result = '6'
        case 3:
            secondMaxFrequency = cardCopy.count( findMostCommon(cardCopy) )
            match secondMaxFrequency:
                case 2:
                    result = '5'
                case _:
                    result = '4'
        case 2:
            secondMaxFrequency = cardCopy.count( findMostCommon(cardCopy) )
            match secondMaxFrequency:
                case 2:
                    result = '3'
                case _:
                    result = '2'
        case 1:
            result = '1'
        case _:
            raise RuntimeError("DON'T PANIC")

    returnValue = result
    for i in card:
        returnValue += f'0{i}' if i < 10 else f'{i}'
    return int(returnValue)

import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")
with open(filename, 'r') as f:
    inputArray = [i.strip() for i in f.readlines()]
givenHands = [i.split(' ') for i in inputArray]
organisedHands = []

for hand in givenHands:
    cardToIntDict = {'A': 14, 'K': 13, 'Q': 12, 'J': 'J', 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    cards = [cardToIntDict[i] for i in hand[0]]
    bid = int(hand[1])

    grade = gradeCard(list(cards))

    if 'J' in cards:
        mostCommon = findMostCommon([i for i in cards if i != 'J'])
        cards = [i if i != 'J' else mostCommon for i in cards]
    organisedHands.append([cards, bid, grade])

organisedHands.sort(key=lambda x: x[2])

total = 0

for index, hand in enumerate(organisedHands):
    cards = hand[0]
    bid = hand[1]
    grade = hand[2]
    total += bid * (index + 1)

print(total)

# more than 250482910
# less than 250608053