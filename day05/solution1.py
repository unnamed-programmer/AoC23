with open('day05/input.txt', 'r') as f:
    inputArray = f.readlines()
seeds = [int(i) for i in inputArray[0].split(':')[-1].strip('\n').split(' ') if i]
index = 3
mapTables = [[] for _ in range(7)]
for mapTable in mapTables:
    while inputArray[index] != '\n':
        temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
        mapTable.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
        index += 1
    index += 2
mappedSeeds = [[i] for i in seeds]
for seed in mappedSeeds:
    for seedIndex, mapTable in enumerate(mapTables):
        for seedMap in mapTable:
            if seed[seedIndex] >= seedMap[0] and seed[seedIndex] < seedMap[1]:
                seed.append(seed[seedIndex] + seedMap[2])
        if len(seed) == seedIndex + 1:
            seed.append(seed[seedIndex])
print(min(mappedSeed[-1] for mappedSeed in mappedSeeds))