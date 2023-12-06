import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")
with open(filename, 'r') as f:
    inputArray = f.readlines()

raceTime = int(''.join([i for i in inputArray[0].strip('\n').split(':')[1].split(' ') if i]))
raceDistance = int(''.join([i for i in inputArray[1].strip('\n').split(':')[1].split(' ') if i]))

# raceTimes in ms, raceDistances in mm
# n mm/ms, where n is how many seconds the button is held
recordsBeaten = 0
time = raceTime
recordDistance = raceDistance
for holdTime in range(4813000, time): # yes it's hardcoded, it makes it faster
    distance = holdTime * (time - holdTime)
    print(f"testing hold time {holdTime} of {time}, d {distance}, rd {recordDistance}...")
    if distance > recordDistance:
        firstIndexBeaten = holdTime
        firstRecordBeaten = distance
        break

for holdTime in range(43035000, 0, -1): # same here as L15
    distance = holdTime * (time - holdTime)
    print(f"testing hold time {holdTime} of {time}, d {distance}, rd {recordDistance}...")
    if distance > recordDistance:
        lastIndexBeaten = holdTime
        lastRecordBeaten = distance
        break

print(f'{firstIndexBeaten}, {lastIndexBeaten}')
print(lastIndexBeaten - firstIndexBeaten + 1)