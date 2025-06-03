#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # length = len(arr)
    # print("line 18", length)

    length = len(arr)

    listAboveZero = 0
    listAtZero = 0
    listBelowZero = 0

    for a in range(len(arr)):
        # print("line 21", arr[a])
        if arr[a] < 0:
            listAboveZero += 1
        elif arr[a] > 0:
            listBelowZero += 1
        elif arr[a] == 0:
            listAtZero += 1

    aboveZeroRatio = listAboveZero/length
    belowZeroRatio = listBelowZero/length
    atZeroRatio = listAtZero/length

    print("{:.6f}".format(belowZeroRatio)) 
    print("{:.6f}".format(aboveZeroRatio))
    print("{:.6f}".format(atZeroRatio))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
