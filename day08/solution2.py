import os
import math
from functools import reduce

def getPrimeFactors(n: int) -> list[int]:
    factors = []
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
directions = inputArray[0].strip()

def findElementMap(inputArray):
    elementMap = {}
    for i in range(2, len(inputArray)):
        line = inputArray[i]
        instruction = line.split('=')[0].strip()
        definition = line.split('=')[1].strip()
        definition = "".join(char for char in definition if char not in "() ").split(',')
        elementMap[instruction] = definition
    return elementMap

elementMap = findElementMap(inputArray)

answersEndingWithA = [key[0] for key in elementMap.items() if key[0][-1] == 'A']
tries = []

for startItem in answersEndingWithA:
    answer = startItem
    currentTries = 0
    continuing = True
    while continuing:
        for direction in directions:
            element = elementMap[answer]
            answer = element[0] if direction == 'L' else element[1]
            currentTries += 1
            if answer[-1] == 'Z': continuing = False; break
            if currentTries >= 100000: raise RuntimeError
    tries.append(currentTries)

# find LCM: split into prime factors, then multiply the common ones up?
primeFactors = [getPrimeFactors(number) for number in tries]

tempPF = []
for primeFactor in primeFactors:
    if isinstance(primeFactor, int):
        tempPF.append(primeFactor)
    else:
        tempPF.extend(iter(primeFactor))
primeFactors = tempPF

lowComMul = reduce(lambda x, y: math.lcm(x, y), primeFactors)

print(lowComMul)