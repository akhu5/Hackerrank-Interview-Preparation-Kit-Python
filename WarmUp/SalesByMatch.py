#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #My soln
    counter = 0
    freq_dict = {}
    for i in range(n):
        if ar[i] in freq_dict:
            freq_dict[ar[i]] += 1
        else:
            freq_dict[ar[i]] = 1
    for i in freq_dict.keys():
        if freq_dict[i] >= 2:
            counter += freq_dict[i] // 2
    return counter

def sockMerchant_optimal(n, ar):
    #NOT my soln
    socks, pairs = Counter(ar), 0
    for s in socks: pairs += socks[s] // 2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()