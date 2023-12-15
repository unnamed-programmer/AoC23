import os

def hashString(s: str) -> int:
    hashVal = 0
    for char in s:
        hashVal += ord(char)
        hashVal *= 17
        hashVal %= 256
    return hashVal

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
inputArray = inputArray[0].strip('\n').split(',')
boxes = [[] for _ in range(256)]

for step in inputArray:
    boxToOp = hashString(step)
    if '-' in step: # remove
        for i in range(len(boxes[boxToOp])):
            if step.split('-')[0] in boxes[boxToOp][i]:
                del boxes[boxToOp][i]
    elif '=' in step: # set box to thing
        for i in range(len(boxes[boxToOp])):
            if step.split('=')[0] in boxes[boxToOp][i]:
                boxes[boxToOp][i] = (step.split('=')[0], step[-1])
        boxes[boxToOp].append((step.split('=')[0], step[-1]))
    else: raise RuntimeError("Oops")

print('dingus')
total = 0
for boxIndex, box in enumerate(boxes):
    for lensIndex, lens in enumerate(box):
        total += (boxIndex + 1) * (lensIndex + 1) * int(lens[1])

print(total)

# 6179429 too high