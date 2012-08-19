#Project Euler - Problem 24
#Language: Python2
#Time of Completion: 20-08-2012 00:12 IST

#---IMPORT SPACE----------
import sys
import math

print (1000000 - 2*math.factorial(9) -6*math.factorial(8)-6*math.factorial(7)-2*math.factorial(6)-5*math.factorial(5)-1*math.factorial(4)-2*math.factorial(3)-1*math.factorial(2)-math.factorial(1)-math.factorial(0))

#Confirm if this sums to zero

#Given m symbols, output the correct nth lexicological ordering. For now, I'll code only for n<=10
m = int(sys.argv[1])
n = int(sys.argv[2])
symbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
symlist = [symbols[x] for x in xrange(m)]

def lex_order(n,symlist):
    k = ""
    t = n
    i = len(symlist)
    if t > math.factorial(i) :
	t = n%math.factorial(i)
    while len(symlist)-1>0:
	q = math.factorial(len(symlist)-1)
	r = t/q
	t = t%q
	print r
	print symlist[r]
	k = k+symlist[r]
	print k
	symlist.remove(symlist[r])
    return k

print lex_order(n,symlist)