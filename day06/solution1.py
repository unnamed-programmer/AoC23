import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    inputArray = f.readlines()

raceTimes = [int(i) for i in inputArray[0].strip('\n').split(':')[1].split(' ') if i]
raceDistances = [int(i) for i in inputArray[1].strip('\n').split(':')[1].split(' ') if i]

# raceTimes in ms, raceDistances in mm
# n mm/ms, where n is how many seconds the button is held

recordsBeaten = [0 for _ in range(len(raceTimes))]

for raceNum in range(len(raceTimes)):
    time = raceTimes[raceNum]
    recordDistance = raceDistances[raceNum]
    for holdTime in range(time):
        distance = holdTime * (time - holdTime)
        if distance > recordDistance:
            recordsBeaten[raceNum] += 1

total = 1
for item in recordsBeaten:
    total *= item

print(total)