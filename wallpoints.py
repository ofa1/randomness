#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#

import math

def solve(h, wallPoints, lengths):
    # Write your code here
    max_height = 0
    for i in range(len(wallPoints)):
        height_needed = math.ceil(float(wallPoints[i]) - (lengths[i]*0.25) - float(h))
        max_height = max(height_needed, max_height)
        print("Got height", max_height, "height needed", height_needed)
    return max_height

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    print(answer)

    # fptr.write(str(answer) + '\n')

    # fptr.close()
