import os
from enum import Enum
from copy import deepcopy

def getInput():
    currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
    filename = os.path.join(currentPath, "input.txt")
    with open(filename, 'r') as f:
        inputArray = f.readlines()
    return inputArray

inputArray = getInput()
tileMap = [_.strip() for _ in inputArray]
tilesEnergised = [[False for _ in n] for n in tileMap]
beams = []

def printTable():
    global tilesEnergised
    print()
    for i in tilesEnergised:
        for j in i:
            print('#' if j else '.', end='')
        print()

class Dir(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Beam:
    def __init__(self, direction: Dir, location: list[int], tileMap: list[str], continuing: bool = True):
        self.direction = direction
        self.location = location
        self.tileMap = tileMap
        self.continuing = continuing

    def isContinuing(self):
        return self.continuing

    def move(self):
        match self.direction:
            case Dir.UP:
                self.location[1] -= 1
            case Dir.LEFT:
                self.location[0] -= 1
            case Dir.DOWN:
                self.location[1] += 1
            case Dir.RIGHT:
                self.location[0] += 1
        if self.location[0] not in range(len(self.tileMap[0])) or self.location[1] not in range(len(self.tileMap)): self.continuing = False

    def handleTile(self):
        global tilesEnergised
        global beams
        currentTile = tileMap[self.location[1]][self.location[0]]
        tilesEnergised[self.location[1]][self.location[0]] = True
        # printTable()
        print('.', end ='')
        match currentTile:
            case '.':
                pass
            case '\\':
                match self.direction:
                    case Dir.UP: self.direction = Dir.LEFT
                    case Dir.LEFT: self.direction = Dir.UP
                    case Dir.DOWN: self.direction = Dir.RIGHT
                    case Dir.RIGHT: self.direction = Dir.DOWN
            case '/':
                match self.direction:
                    case Dir.UP: self.direction = Dir.RIGHT
                    case Dir.LEFT: self.direction = Dir.DOWN
                    case Dir.DOWN: self.direction = Dir.LEFT
                    case Dir.RIGHT: self.direction = Dir.UP
            case '|':
                if self.direction not in [Dir.UP, Dir.DOWN]:
                    beams.append(Beam(Dir.UP, self.location.copy(), deepcopy(self.tileMap)))
                    self.direction = Dir.DOWN
            case '-':
                if self.direction not in [Dir.LEFT, Dir.RIGHT]:
                    beams.append(Beam(Dir.LEFT, self.location.copy(), deepcopy(self.tileMap)))
                    self.direction = Dir.RIGHT
            case _:
                raise RuntimeError()

beams.append(Beam(Dir.RIGHT, [0, 0], tileMap))
prevTilesEnergised = []

while any(beam.isContinuing() for beam in beams):
    prevTilesEnergised.insert(0, deepcopy(tilesEnergised))
    for beam in beams:
        if beam.isContinuing():
            beam.handleTile()
            beam.move()
    if len(prevTilesEnergised) > 5:
        if tilesEnergised == prevTilesEnergised[4]: break
        prevTilesEnergised.pop()

total = 0
for i in tilesEnergised:
    for j in i:
        # print('#' if j else '.', end='')
        if j: total += 1
    # print()

print(total)