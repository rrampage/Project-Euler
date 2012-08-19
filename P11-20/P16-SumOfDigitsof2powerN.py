#Project Euler - Problem 16
#Language: Python2
#Time of Completion: 19-08-2012 18:28 IST

#To find sum of digits of an integer m raised to a power n

#----IMPORT SPACE-------#
import sys
import math


def digitsum(n):
    """Returns sum of the digits of the number"""
    k = int(n)
    a = 0
    while k!= 0 :
        t = k%10
        k = k/10
        a = a+t
    return a

m = int(sys.argv[1])
n = int(sys.argv[2])
p = math.pow(m,n)
print digitsum(p)