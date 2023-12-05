import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

# GAME PLAN

# create lists:
# seeds
# seed -> soil
# soil -> fertilizer
# fertilizer -> water
# water -> light
# light -> temperature
# temperature -> humidity
# humidity -> location

# each one 2d arrays - [destinationStart, sourceStart, range]
# somehow figure out the logic to unpack these arrays and pass individual numbers into that and get mapped ones back out
# cascade references - hppefully end up with locations for each of the seeds

# find lowest location number corresponding to a seed

# seeds list
index = 0
seeds = [int(i) for i in
        inputArray[index]
        .split(':')[-1]
        .strip('\n')
        .split(' ')
        if i]



# Parse inputs and generate map table
# change from [destStart, srcStart, range]
# to [srcStart, srcEnd, offset]

index += 3
seedsToSoilMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    seedsToSoilMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

index += 2
soilToFertilizerMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    soilToFertilizerMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

index += 2
fertilizerToWaterMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    fertilizerToWaterMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

index += 2
waterToLightMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    waterToLightMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

index += 2
lightToTemperatureMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    lightToTemperatureMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

index += 2
temperatureToHumidityMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    temperatureToHumidityMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

index += 2
humidityToLocationMap = []
while inputArray[index] != '\n':
    temp = [int(i) for i in inputArray[index].strip('\n').split(' ') if i]
    humidityToLocationMap.append([temp[1], temp[1] + temp[2], temp[0] - temp[1]])
    index += 1

print("Finished creating map arrays")


# Map seeds to final results
mappedSeeds = [[i] for i in seeds]
for seed in mappedSeeds:
    seedIndex = 0
    for seedMap in seedsToSoilMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
            seed.append(seed[seedIndex] + seedMap[2])
            print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
        else:
            print(f"{seed[seedIndex]} does NOT map in {seedMap}")
    if len(seed) == seedIndex + 1:
        seed.append(seed[seedIndex])

    seedIndex += 1
    for seedMap in soilToFertilizerMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
            seed.append(seed[seedIndex] + seedMap[2])
            print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
        else:
            print(f"{seed[seedIndex]} does NOT map in {seedMap}")
    if len(seed) == seedIndex + 1:
        seed.append(seed[seedIndex])

    seedIndex += 1
    for seedMap in fertilizerToWaterMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
            seed.append(seed[seedIndex] + seedMap[2])
            print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
        else:
            print(f"{seed[seedIndex]} does NOT map in {seedMap}")
    if len(seed) == seedIndex + 1:
        seed.append(seed[seedIndex])

    seedIndex += 1
    for seedMap in waterToLightMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
            seed.append(seed[seedIndex] + seedMap[2])
            print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
        else:
            print(f"{seed[seedIndex]} does NOT map in {seedMap}")
    if len(seed) == seedIndex + 1:
        seed.append(seed[seedIndex])

    seedIndex += 1
    for seedMap in lightToTemperatureMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
            seed.append(seed[seedIndex] + seedMap[2])
            print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
        else:
            print(f"{seed[seedIndex]} does NOT map in {seedMap}")
    if len(seed) == seedIndex + 1:
        seed.append(seed[seedIndex])

    seedIndex += 1
    for seedMap in temperatureToHumidityMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
            seed.append(seed[seedIndex] + seedMap[2])
            print(f"{seed[seedIndex]} maps to {seed[seedIndex + 1]} in {seedMap}")
        else:
            print(f"{seed[seedIndex]} does NOT map in {seedMap}")
    if len(seed) == seedIndex + 1:
        seed.append(seed[seedIndex])

    seedIndex += 1
    for seedMap in humidityToLocationMap:
        if seed[seedIndex] >= seedMap[0] and seed[seedIndex] <= seedMap[1]:
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