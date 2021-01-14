#!/bin/python3

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    len_str = len(s)
    for i in range(len_str):
        if s[i] == "a":
            count += 1
    total_no = n // len_str
    amp = n % len_str
    count = count * total_no
    for i in range(amp):
        if s[i] == "a":
            count += 1
    return int(count)

def repeatedString_opt(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
