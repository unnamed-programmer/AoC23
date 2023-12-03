import os

def check(in1, in2, exp1, exp2):
    if in1 == exp1 and in2 == exp2:
        print("OK")
    else: raise RuntimeError(f"{in1} NOT {exp1} or {in2} NOT {exp2}")

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numList = []

    for line in f.readlines():
        line = line.strip()
        firstNum = ""
        lastNum = ""
        charString = ""

        print(line)

        for char in line:
            if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if firstNum == "":
                    firstNum = char
                lastNum = char
                print("DIGIT " + char)

            else:
                charString += char
                if any(digit in charString for digit in digits):
                    needTrim = True
                    while needTrim:
                        try: digits.index(charString)
                        except: charString = charString[1:]
                        else: needTrim = False

                    if firstNum == "":
                        firstNum = str(digits.index(charString))
                    lastNum = str(digits.index(charString))
                    print("WORD " + charString)

                    charString = charString[1:]

        print(f"{firstNum}, {lastNum}")

        numList.append(firstNum + lastNum)

        #print(numList)
        print()


    sum = 0
    while numList:
        sum += int(numList.pop())
    print(sum)