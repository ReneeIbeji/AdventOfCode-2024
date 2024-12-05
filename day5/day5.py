
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
            total += int(line[len(line) // 2])
        else:
            print(fixLine(line, rules))
        index += 1

    return total


def part2(file):
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
        if not checkLine(line, rules):
            fix = fixLine(line, rules)
            total += int(fix[len(fix) // 2])

        index += 1

    return total


def checkLine(line,rules):
    line = line.split(",")

    for pageNum in range(len(line)):
        page = line[pageNum]
        for rule in rules:
            if rule[0] == page:
                for i in range(0,min(pageNum,len(page))):
                    if rule[1] == line[i]:
                        return False
    return True


def fixLine(line,rules):
    line = line.split(",")
    return fixSegment(line, rules)


def fixSegment(section,rules):
    if len(section) == 1 or len(section) == 0:
        return section

    before = []
    after = []
    for rule in rules:
        if rule[0] == section[0]:
            if rule[1] in section:
                after.append(rule[1])

    for page in section:
        if page not in after and page != section[0]:
            before.append(page)
    result = fixSegment(before, rules)
    result.append(section[0])

    result = result + fixSegment(after, rules)

    return result


file = fileToArray("puzzleInput.txt")
print("part 1:", part1(file))
print("part 2:", part2(file))

