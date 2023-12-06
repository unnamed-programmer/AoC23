import os
from re import M
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

index = 0
tempSeeds = [int(i) for i in
             inputArray[index]
            .split(':')[-1]
            .strip('\n')
            .split(' ')
             if i]

print("Finding seeds")
seeds = []
for i in range(0, len(tempSeeds), 2):
    start = tempSeeds[i]
    length = tempSeeds[i + 1]
    for j in range(start, start + length, 100000):
        seeds.append(j)
        print(j)
print("Found seeds")

# Parse inputs and generate map table
# change from [destStart, srcStart, range]
# to [srcStart, srcEnd, offset]

index += 3

mapTables = [[] for _ in range(7)]
for mapTable in mapTables:
    while inputArray[index] != '\n':
        temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
        mapTable.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
        index += 1
    index += 2

print("Finished creating map arrays")

# Map seeds to final results
mappedSeeds = [[i] for i in seeds]
for seed in mappedSeeds:
    for seedIndex, mapTable in enumerate(mapTables):
        for seedMap in mapTable:
            if seed[seedIndex] >= seedMap[0] and seed[seedIndex] < seedMap[1]:
                seed.append(seed[seedIndex] + seedMap[2])
                print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
            else:
                print(f"{seed[seedIndex]} does NOT map in {seedMap}")
        if len(seed) == seedIndex + 1:
            seed.append(seed[seedIndex])

lowestNumber = 99999999999999999
for mappedSeed in mappedSeeds:
    if mappedSeed[-1] < lowestNumber:
        lowestNumber = mappedSeed[-1]

print(lowestNumber)