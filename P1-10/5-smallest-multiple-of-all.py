#Project Euler - Problem 5
#Language: Python
#Time of Completion: 17-08-2012 22:27 IST

#Smallest number divisible by all numbers from 1-20
#Prime numbers from 1-20:
#2,3,5,7,11,13,17,19
#Higher powers of primes from 1-20: 2^4 =16 and 3^2 = 9
#Therefore, product = 16*9*5*7*11*13*17*19 = 232792560
#Finds all primes upto n

#---------IMPORT SPACE-------------#
import sys


#Using the primeLister function I used to solve Problem 7.
def primeLister(n,l = [2,3,5,7,11,13]):
    rem = []
    x = max(l)
    while max(l)<n :
        x = x+2
        for y in l :
            if x%y == 0 :
                rem.append(x)
                break
        if x not in rem:
            l.append(x)
    return l

#Finds powers of numbers upto n
def powerfinder(n):
    primes = primeLister(n)
    while (max(primes)>n):
	primes.remove(max(primes))
    powerlist = [1]*len(primes)
    power = 2
    for x in primes:
        while (x**power)<=n:
            powerlist[primes.index(x)]=power
            power = power+1
        power = 2
    return primes,powerlist

def minNumDivUptoN(n):
    n = int(n)
    ans = powerfinder(n)
    print ans[0]
    print ans[1]
    prod = [ans[0][x]**ans[1][x] for x in range(len(ans[0]))]
    fin = 1
    for x in prod :
        fin = fin*x
    return fin

print minNumDivUptoN(sys.argv[1])

#-----DEPRECIATED------#

#Original method used to find primes upto n. Highly unoptimized. Takes HUGE time for even moderate n ~ 10000)
def primesUptoN(n):
    b = range(3,n+1,2) #Create a range of n numbers
    c = []
    for x in b:
        for y in range(3,x,2) :
            if x%y == 0:
                c.append(x)
                break
    for x in c:
        b.remove(x)
    return b