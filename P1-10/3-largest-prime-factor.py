#Project Euler - Problem 3
#Language: Python
#Time of Completion: 17-08-2012 16:25 IST

import sys
import math

#Finds all factors of an integer n
def factor(n):
    """Returns a sorted array of the factors of an integer n"""
    n = int(n)
    mat = int(math.ceil(math.sqrt(n)))
    fac = []
    rem = []
    for x in range(19,mat,2):
        if (n%x  == 0):
           fac.append(x)
           rem.append(n/x)
    for x in range(len(rem)):
        fac.append(rem[x])
    fac.sort()
    return fac

def popper(arr):
    arr.sort()
    b = []
    for x in range(1,len(arr)):
        for y in range(x-1):
            if (arr[x]%arr[y])==0 :
                b.append(arr[x])
    c = list(set(b))
    a = list(arr)
    for x in range(len(c)):
        a.remove(c[x])
    return a

a = factor(sys.argv[1])
print a
b = popper(a)
print max(b)