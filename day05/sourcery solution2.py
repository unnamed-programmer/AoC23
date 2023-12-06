import os

def map_seeds(seeds, mapping):
    for seed in seeds:
        seedIndex = 0
        for seedMap in mapping:
            if seed[seedIndex] >= seedMap[0] and seed[seedIndex] < seedMap[1]:
                seed.append(seed[seedIndex] + seedMap[2])
        if len(seed) == seedIndex + 1:
            seed.append(seed[seedIndex])
        seedIndex += 1

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

index = 0
tempSeeds = [int(i) for i in inputArray[index].split(':')[-1].strip('\n').split(' ') if i]

# Finding seeds
seeds = [j for i in range(0, len(tempSeeds), 2) for j in range(tempSeeds[i], tempSeeds[i] + tempSeeds[i + 1])]

# Parse inputs and generate map tables
maps = []
for _ in range(6):
    index += 3
    map_table = []
    while inputArray[index] != '\n':
        temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
        map_table.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
        index += 1
    maps.append(map_table)

# Map seeds to final results
mappedSeeds = [[i] for i in seeds]
for mapping in maps:
    map_seeds(mappedSeeds, mapping)

# Find the lowest number
lowestNumber = min(mappedSeed[-1] for mappedSeed in mappedSeeds)

print(lowestNumber)