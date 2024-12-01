
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
    list1 = []
    list2 = []

    for line in file:
        lineSplit = line.split("   ")
        list1.append(int(lineSplit[0]))
        list2.append(int(lineSplit[1]))

    list1.sort()
    list2.sort()

    totalDistance = 0
    for i in range(len(list1)):
        totalDistance += abs(list2[i] - list1[i])

    return totalDistance


def part2(file):
    list1 = []
    list2 = []

    for line in file:
        lineSplit = line.split("   ")
        list1.append(int(lineSplit[0]))
        list2.append(int(lineSplit[1]))

    score = 0
    for value in list1:
        score += list2.count(value) * value

    return score


file = fileToArray("puzzleInput.txt")

print("part 1:",str(part1(file)))
print("part 2:",str(part2(file)))

