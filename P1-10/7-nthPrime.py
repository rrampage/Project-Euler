#Project Euler - Problem 7
#Language: Python
#Time of Completion: 18-08-2012 02:25 IST

#The 10,001st Prime!
#Took 19.04 sec to find the 10,001st prime WITH bootstrapping (a crude form of Dynamic Programming)
#Took 40.91 sec to find the 10,001st prime WITHOUT bootstapping (directly)

#-----IMPORT SPACE-------#

import sys

def primelister(n,l = [2,3,5,7,11,13,17,19,23,29]):
    rem = []
    x = max(l)
    while len(l)<n :
        x = x+2
        for y in l :
            if x%y == 0 :
                rem.append(x)
                break
        if x not in rem:
            l.append(x)
    return l

def bootstrapper(n):
    n = int(n)
    if n > 10000 :
        k = primelister(n/100)
        j = primelister(n/20,k)
        l = primelister(n/4,j)
        m = primelister(n/2,l)
        o = primelister(n/2,m)
        p = primelister(n,o)
        return p
    return primelister(n)

print max(bootstrapper(sys.argv[1]))
#print max(primelister(int(sys.argv[1])))