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

    print("Game no.: ", gameNumber)
    print("Content: ", gameContent)
    print("Sections: ", gameSections)

    minRed = 0
    minGreen = 0
    minBlue = 0

    for section in gameSections:
        section = section.split(',')
        for subsection in section:
            subsection = subsection[1::]
            number = int(subsection.split(' ')[0])
            colour = subsection.split(' ')[1]
            print("Section: ", number, colour)
            if colour == 'red':
                if number > minRed:
                    minRed = number
            elif colour == 'green':
                if number > minGreen:
                    minGreen = number
            elif colour == 'blue':
                if number > minBlue:
                    minBlue = number
            else:
                raise RuntimeError()

    total += minRed * minGreen * minBlue

    print("minRed: ", minRed, ", minGreen: ", minGreen, ", minBlue: ", minBlue)
    print()

print(total)