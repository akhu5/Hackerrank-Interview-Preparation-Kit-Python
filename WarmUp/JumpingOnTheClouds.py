#!/bin/python3

import os

def jumpingOnClouds(c):
    jump = i = 0
    while i < len(c) - 2:
        i = i + 1 if int(c[i+2]) == 1 else i + 2
        jump += 1
    if i < len(c) - 1:
        jump += 1
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()