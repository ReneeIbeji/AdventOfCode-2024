import re


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
    total = 0
    for line in file:
        results = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",line)
        print(results)
        for operation in results:
            operation = operation[4:]
            operation = operation[:len(operation) - 1]
            operation = operation.split(",")
            total += int(operation[0]) * int(operation[1])

    return total


def part2(file):
    total = 0
    doOp = True
    for line in file:

        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

        results = re.findall(pattern, line)

        for operation in results:
            if operation == "don't()":
                doOp = False
                continue
            if operation == "do()":
                doOp = True
                continue
            if doOp:
                operation = operation[4:]
                operation = operation[:len(operation) - 1]
                operation = operation.split(",")
                total += int(operation[0]) * int(operation[1])

    return total


file = fileToArray("puzzleInput.txt")
print("part 1:", part1(file))
print("part 2:", part2(file))

