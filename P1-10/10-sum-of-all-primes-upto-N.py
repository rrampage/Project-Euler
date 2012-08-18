#Project Euler - Problem 10
#Language: Python2
#Time of Completion: 18-08-2012 05:27 IST

#Sum of All Primes upto 2 million

#-------IMPORT SPACE-----------#
import sys

def primeLister(n,l = [2,3,5,7,11,13]):
    rem = max(l)+1
    x = max(l)
    while max(l)<n :
        x = x+2
        for y in l :
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

print(sum(bootstrapper(sys.argv[1])))