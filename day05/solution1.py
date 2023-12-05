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
