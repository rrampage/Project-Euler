#Project Euler - Problem 12
#Language: Python2
#Time of Completion: 19-08-2012 15:47 IST

#First Triangle Number with n divisors
#A Triangle number is n*(n+1)/2

#----IMPORT SPACE------------------#
import sys
import math

def calc_triangle(n):
    int(n)
    return n*(n+1)/2

#Reuse for Problem 5. Slightly modified
def factorLister(n):
    x = 2
    factors = []
    while x<math.ceil(math.sqrt(n)) :
        x = x+1
        if n%x == 0 :
            factors.append(x)
	    factors.append(n/x)
    factors.sort()
    factors.append(n)
    return factors

n = int(sys.argv[1])
num = 7
k = 28
factors = []

while len(factors)<=n :
    num = num + 1
    k = calc_triangle(num)
    factors = factorLister(k)
    print num

print num
print k
