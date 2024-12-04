from enum import Enum

def fileToArray(fileName):
    result = []
    file = open(fileName,"r")
    line = file.readline()
    while line != "":
        line = line.strip("\n")
        result.append(line)
        line = file.readline()

    return result


Direction2 = Enum('Direction', [('UP', 1), ('UPRIGHT', 2), ('RIGHT', 3), ('DOWNRIGHT', 4), ('DOWN', 5), ('DOWNLEFT',6), ('LEFT',7), ('UPLEFT',8)])


class Direction(Enum):
    UP = 1
    UPRIGHT = 2
    RIGHT = 3
    DOWNRIGHT = 4
    DOWN = 5
    DOWNLEFT = 6
    LEFT = 7
    UPLEFT = 8


def part1(file):
    word = "MAS"
    total = 0
    for y in range(len(file)):
        line = file[y]
        for x in range(0,len(line)):
            if line[x] == 'X':
                pos = (x,y)
                total += 1 if checkIfPresent(file, word, Direction.UP, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.UPRIGHT, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.RIGHT, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.DOWNRIGHT, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.DOWN, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.DOWNLEFT, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.LEFT, pos) else 0
                total += 1 if checkIfPresent(file, word, Direction.UPLEFT, pos) else 0

    return total


def checkIfPresent(file,word,dir,pos):
    if len(word) == 0:
        return True

    if dir == Direction.UP:
        pos = (pos[0],pos[1] + 1)
    if dir == Direction.UPRIGHT:
        pos = (pos[0] + 1,pos[1] + 1)
    if dir == Direction.RIGHT:
        pos = (pos[0] + 1,pos[1])
    if dir == Direction.DOWNRIGHT:
        pos = (pos[0] + 1,pos[1] - 1)
    if dir == Direction.DOWN:
        pos = (pos[0],pos[1] - 1)
    if dir == Direction.DOWNLEFT:
        pos = (pos[0] - 1,pos[1] - 1)
    if dir == Direction.LEFT:
        pos = (pos[0] - 1,pos[1])
    if dir == Direction.UPLEFT:
        pos = (pos[0] - 1,pos[1] + 1)

    if pos[0] >= len(file[0]) or pos[0] < 0 or pos[1] >= len(file) or pos[1] < 0:
        return False

    char = word[0]

    if file[pos[1]][pos[0]] == char:
        return checkIfPresent(file, word[1:], dir, pos)
    else:
        return False


def part2(file):
    total = 0
    for y in range(len(file)):
        line = file[y]
        for x in range(0,len(line)):
            if line[x] == 'A':
                pos = (x,y)
                total += 1 if checkIfXPresent(file, pos) else 0

    return total


def checkIfXPresent(file,pos):
    if pos[0] - 1 < 0 or pos[0] + 1 >= len(file[0]) or pos[1] - 1 < 0 or pos[1] + 1 >= len(file):
        return False

    return checkPair(file[pos[1]-1][pos[0]-1], file[pos[1]+1][pos[0]+1]) and checkPair(file[pos[1]+1][pos[0]-1],file[pos[1]-1][pos[0]+1])


def checkPair(a,b):
    return (a == "M" and b == "S") or (a == "S" and b == "M")


file = fileToArray("puzzleInput.txt")
print("part 1:", part1(file))
print("part 2:", part2(file))

