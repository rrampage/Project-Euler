#Project Euler - Problem 20
#Language: Python2
#Time of Completion: 19-08-2012 18:30 IST

#Reuses code from Problem 16

#To find sum of digits of the Factorial of a number n

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

n = int(sys.argv[1])
p = math.factorial(n)
print digitsum(p)