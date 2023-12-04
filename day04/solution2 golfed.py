with open('input.txt', 'r') as f: inputArray = f.readlines()
scratchCard = {int(line.split(':')[0].split(' ')[-1]): ([int(i) for i in line.split(':')[1].strip('\n').split('|')[0].split(' ') if i != ''], [int(i) for i in line.split(':')[1].strip('\n').split('|')[1].split(' ') if i != ''], 1) for line in inputArray}
for index in scratchCard:
    for i in range(1, sum(int(chosenNumber in scratchCard[index][0]) for chosenNumber in scratchCard[index][1]) + 1): scratchCard[index + i] = (scratchCard[index + i][0], scratchCard[index + i][1], scratchCard[index + i][2] + scratchCard[index][2])
print(sum(scratchCard[index][2] for index in scratchCard))