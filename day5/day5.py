
def fileToArray(fileName):
    result = []
    file = open(fileName,"r")
    line = file.readline()
    while line != "":
        line = line.strip("\n")
        result.append(line)
        line = file.readline()

    return result


def part1(file):
    index = 0
    total = 0
    line = file[index]
    rules = []


    while line != "":
        line = line.split("|")
        rules.append((line[0],line[1]))
        index += 1
        line = file[index]

    index += 1

    while index < len(file):
        line = file[index]
        if checkLine(line, rules):
            line = line.split(",")
            print(line)
            total += int(line[len(line) // 2])
            print(total)
        index += 1

    return total


def checkLine(line,rules):
    line = line.split(",")

    for pageNum in range(len(line)):
        page = line[pageNum]
        for rule in rules:
            if rule[0] == page:
                print(rule)
                for i in range(0,min(pageNum,len(page))):
                    print(line[i])
                    if rule[1] == line[i]:
                        return False
    return True



file = fileToArray("puzzleInput.txt")
print("part 1:", part1(file))
# print("part 2:", part2(file))

