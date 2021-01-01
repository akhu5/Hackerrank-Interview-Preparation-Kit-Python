#!/bin/python3

def countingValleys(steps, path):
    alt = valley = 0
    valleyStart = True
    for i in range(steps):
        if path[i] == "D":
            alt -= 1
        else:
            alt += 1
        if alt < 0 and valleyStart is True:
            valley += 1
            valleyStart = False
        if alt == 0:
            valleyStart = True
    return valley

def countingValleys_optimal(steps, path):
    UD = {'U': 1, 'D': -1}
    sea_level = 0
    valley = 0
    for step in path:
        sea_level = sea_level + UD[step]
        if not sea_level and step == 'U':
            valley += 1
    return valley

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys_optimal(steps, path)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()