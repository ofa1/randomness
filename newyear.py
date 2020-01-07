#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys
from operator import sub

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    for i in range(0, n):
        for j in range(0,n):
            
    return sum(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
