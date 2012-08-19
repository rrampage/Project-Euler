#Project Euler - Problem 15
#Language: Python2
#Time of Completion: 19-08-2012 23:00 IST

#To find number of ways possible to reach from top-left to bottom-right of an N x N grid

#----IMPORT SPACE-------#
import sys
import math

n = int(sys.argv[1])
r = int(sys.argv[2])

def C(n,r):
    n = int(n)
    r = int(r)
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

print C(n,r)