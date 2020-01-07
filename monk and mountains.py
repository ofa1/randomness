# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/little-monk-and-mountains/
from itertools import chain
def doubleIP():
    ip = input().split(" ")
    a = int(ip[0])
    b = int(ip[1])
    return [a,b]
nq = doubleIP()
n = nq[0]
q = nq[1]
mountains = []
for i in range(0, n):
    ranges = doubleIP()
    start = ranges[0]
    end = ranges[1]+1
    for j in mountains:
        if min(j) > start and max(j) < end:
            j = range(start, end)
        elif min(j) < start and end < max(j):
            break
        elif min(j) < start 
for i in range(0,q):
    xth = int(input())
    print(mountains[xth-1])

