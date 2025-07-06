#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    lengthArr = len(arr)
    # array of length 5

    topFour = sorted(arr, reverse=True)[:4]
    bottomFour = sorted(arr, reverse=False)[:4]

    max = sum(topFour)
    min = sum(bottomFour)

    print("max value", max)

    print ("min value", min)

    print (min, max)

    return max, min

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
