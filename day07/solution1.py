import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "testin.txt")
with open(filename, 'r') as f:
    inputArray = [i.strip() for i in f.readlines()]
givenHands = [i.split(' ') for i in inputArray]

for hand in givenHands:
    cardToIntDict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    card = [cardToIntDict[i] for i in hand[0]]
    bid = int(hand[1])
    print(f'{card}, {bid}')




def gradeCard(card: list[int]) -> list[int]:
    # return (grade, digit0, digit1..4) in int form, g01234
    returnValue = []
    mostCommon = max(card, key=card.count)
    if card.count(mostCommon) == 5:
        returnValue.append(7)
    elif card.count(mostCommon) == 4:
        returnValue.append(6)
    elif card.count(mostCommon) == 3:
        cardCopy = card
        while mostCommon in cardCopy: cardCopy.remove(mostCommon)
        secMostCommon = max(cardCopy, key=cardCopy.count)
        if cardCopy.count(secMostCommon) == 2:
            returnValue.append(5)
        else:
            returnValue.append(4)
    elif card.count(mostCommon) == 2:
        cardCopy = card
        while mostCommon in cardCopy: cardCopy.remove(mostCommon)
        secMostCommon = max(cardCopy, key=cardCopy.count)
        if cardCopy.count(secMostCommon) == 2:
            returnValue.append(3)
        else:
            returnValue.append(2)
    elif card.count(mostCommon) == 1:
        returnValue.append(1)
    else:
        raise RuntimeError("DON'T PANIC")

    returnValue.extend(iter(card))
    
    return returnValue