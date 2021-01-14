#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    d = d%len(a)
    if d == len(a):
        return a
    else:
        for k in range(d):
            i = 0
            j = a[0]
            for i in range(len(a)-1):
                a[i] = a[i+1]
            a[i+1] = j
        return a

def rotLeft_opt(a, d):
    alist = list(a)
    return alist[d:] + alist[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
