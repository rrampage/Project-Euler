#Project Euler - Problem 14
#Language: Python2
#Time of Completion: 19-08-2012 14:52 IST

#The Collatz Conjecture

#-----IMPORT SPACE------
import sys

def collatz(n):
    """Returns number of steps required to reach 1 from n"""
    a = 1
    num = n
    while num!= 1 :
        if num%2 == 0:
            num = num/2
        else:
            num = 3*num +1
        a = a+1
    return a

maxi = 10
num = 13

n = int(sys.argv[1])

for x in xrange(1,n):
    j = collatz(x)
    if j>maxi :       
        maxi = j
	num = x
	print x

print num
print maxi

