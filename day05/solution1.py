import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "testin.txt")

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

index += 3
seedsToSoilMap = []
while inputArray[index] != '\n':
    seedsToSoilMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

index += 2
soilToFertilizerMap = []
while inputArray[index] != '\n':
    soilToFertilizerMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

index += 2
fertilizerToWaterMap = []
while inputArray[index] != '\n':
    fertilizerToWaterMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

index += 2
waterToLightMap = []
while inputArray[index] != '\n':
    waterToLightMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

index += 2
lightToTemperatureMap = []
while inputArray[index] != '\n':
    lightToTemperatureMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

index += 2
temperatureToHumidityMap = []
while inputArray[index] != '\n':
    temperatureToHumidityMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

index += 2
humidityToLocationMap = []
while inputArray[index] != '\n':
    humidityToLocationMap.append([int(i) for i in inputArray[index].strip('\n').split(' ') if i])
    index += 1

raise RuntimeError('FUCKET ERROR - Invalid temperature temperature output')