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
        safe = True
        nums = line.split(" ")
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        allIncreasing = (nums[1] - nums[0] > 0)
        for i in range(0, len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if (diff > 0 and not allIncreasing) or (diff < 0 and allIncreasing):
                safe = False
                break
            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break

        if safe:
            total += 1

    return total


def part2(file):
    total = 0
    for line in file:
        nums = line.split(" ")

        for i in range(len(nums)):
            nums[i] = int(nums[i])

        allCombos = [None for i in range(len(nums) + 1)]
        allCombos[0] = nums
        for i in range(len(nums)):
            allCombos[i + 1] = removeValueFromArray(nums, i)

        for nums in allCombos:
            safe = True
            allIncreasing = (nums[1] - nums[0] > 0)

            for i in range(0, len(nums) - 1):
                diff = nums[i+1] - nums[i]
                if (diff > 0 and not allIncreasing) or (diff < 0 and allIncreasing):
                    safe = False
                    break
                if abs(diff) < 1 or abs(diff) > 3:
                    safe = False
                    break

            if safe:
                print("safe:",line)
                total += 1
                break

    return total


def checkValue(diff,allIncreasing):
    if (diff > 0 and not allIncreasing) or (diff < 0 and allIncreasing):
        return False
    if abs(diff) < 1 or abs(diff) > 3:
        return False

    return True

def removeValueFromArray(array, index):
    newArr = [None for i in range(len(array) - 1)]
    z = 0
    for i in range(len(array)):
        if i != index:
            newArr[z] = array[i]
            z += 1

    return newArr



file = fileToArray("puzzleInput.txt")

print(part1(file))
print(part2(file))
