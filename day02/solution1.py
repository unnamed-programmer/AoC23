# 12 red, 13 green, 14 blue

import os
currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))
filename = os.path.join(currentPath, "input.txt")

with open(filename, 'r') as f:
    gamesArray = f.readlines()

total = 0

for game in gamesArray:
    gameNumber = game.split(':')[0].split(' ')[1]
    gameContent = game.split(':')[1].strip('\n')
    gameSections = gameContent.split(';')
    gamePossible = True

    print("Game no.: ", gameNumber)
    print("Content: ", gameContent)
    print("Sections: ", gameSections)

    for section in gameSections:
        section = section.split(',')
        for subsection in section:
            subsection = subsection[1::]
            number = subsection.split(' ')[0]
            colour = subsection.split(' ')[1]
            print("Section: ", number, colour)
            if colour == 'red':
                if int(number) > 12:
                    gamePossible = False
            elif colour == 'green':
                if int(number) > 13:
                    gamePossible = False
            elif colour == 'blue':
                if int(number) > 14:
                    gamePossible = False
            else:
                raise RuntimeError()

    if gamePossible:
        print('Possible')
        total += int(gameNumber)

    print()

print(total)
