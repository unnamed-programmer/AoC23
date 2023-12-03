import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    numList = []
    for line in f.readlines():
        line = line.strip()
        firstNum = ""
        lastNum = ""
        for char in line:
            if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if firstNum == "":
                    firstNum = char
                lastNum = char
        numList.append(firstNum + lastNum)
    sum = 0
    for num in numList:
        sum += int(num)
    print(sum)