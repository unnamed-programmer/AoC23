def deckRank(hand: str) -> int:
    cards = sorted(hand)
    possibleCards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for i in possibleCards:
        possibleCards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        if cards.count(i) == 5:
            return 6
        elif cards.count(i) == 4:
            return 5
        elif cards.count(i) == 3:
            possibleCards.remove(i)
            return next((4 for j in possibleCards if cards.count(j) == 2), 3)
        elif cards.count(i) == 2:
            possibleCards.remove(i)
            return next((2 for j in possibleCards if cards.count(j) == 2), 1)
    return 0


def higherCard(hand1, hand2) -> bool:
    cardToValMap = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    rank1 = deckRank(hand1)
    rank2 = deckRank(hand2)
    if rank1 != rank2:
        greaterThan = rank1 > rank2
        return greaterThan

    for i in range(len(hand1)):
        digit1 = cardToValMap[hand1[i]]
        digit2 = cardToValMap[hand2[i]]
        greaterThan = digit1 > digit2
        return greaterThan

    raise RuntimeError



import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")
with open(filename, 'r') as f:
    inputArray = f.readlines()

cardsArray = []
for line in inputArray:
    hand, bid = line.split()
    cardsArray.append((hand, bid))

sortedCardsArray = []
for card in cardsArray:
    if not sortedCardsArray:
        sortedCardsArray.append(card)
    else:
        for index in range(len(sortedCardsArray)):
            item = sortedCardsArray[index]
            if higherCard(card[0], item[0]):
                sortedCardsArray.insert(index, card)
                break
sortedCardsArray.reverse()

print(sortedCardsArray)

total = 0
for index, card in enumerate(sortedCardsArray):
    total += int(card[1]) * (index + 1)
    
print(total)