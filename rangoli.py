# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def getRangoliRow(i, n):
    r = ''
    for i in range(i, n+1):
        r += chr(97 + i) + '-'
    r = r[:-1]
    return  r[::-1] + r[1:]

def printRangoli(n):
    l = []
    for i in range(0,n):
        s = getRangoliRow(i, n-1)
        if len(l) >= 1:
            s = s.center(len(l[0]), '-')
            l.insert(0,s)
        l.append(s)
    for r in l:
        print(r)
printRangoli(5)