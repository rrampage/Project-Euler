#Project Euler - Problem 10
#Language: Python2
#Time of Completion: 18-08-2012 06:07 IST

#Sum of All Primes upto 2 million

#-------IMPORT SPACE-----------#
import sys
import math


def quickSum(n):
    sum = 2
    for x in xrange(3,n,2):
	sum = sum+(isPrime(x)*x)
    return sum

def isPrime(x):
    rr = int(math.sqrt(x))+1
    for y in xrange(3,rr,2):
        if x%y == 0 :
	    return 0
    return 1

def sieve(n):
    numbers = range(0, n)
    for prime in numbers:
        if prime < 2:
            continue
        elif prime > n ** 0.5:
            break
        for i in range(prime ** 2, n, prime):
            numbers[i] = 0
    return [x for x in numbers if x > 1]


u = int(sys.argv[1])
#print quickSum(u)
print sum(sieve(u))

#----DEPRECIATED--------#

def primeLister(n,l = [2,3,5,7,11,13]):
    rem = max(l)+1
    x = max(l)
    rr = int(math.sqrt(n))
    while max(l)<n :
        x = x+2
        for y in xrange(3,rr,2):
            if x%y == 0 :
                rem = x
                break
        if x!=rem:
            l.append(x)
    return l

def bootstrapper(n):
    n = int(n)
    if n > 200000 :
	k = primeLister(5000)
    	k2 = primeLister(25000,k)
    	k = primeLister(50000,k2)
    	k2 = primeLister(100000,k)
    	j = primeLister(150000,k2)
    	k = primeLister(200000,k2)
	print max(k), sum(k)
	for x in range(1,int((n-200000)/5000)):
            k = primeLister(200000+5000*x,k)
	    print max(k)
	while(max(k)>n):
	    k.remove(max(k))
        return k
    return primeLister(n)
#print sum(primeLister(u))