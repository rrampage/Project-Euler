#Project Euler - Problem 48
#Language: Python2
#Time of Completion: 19-08-2012 23:48 IST

#---IMPORT SPACE----------
import gmpy

s = gmpy.mpq(0)

for x in xrange(1,1001):
    s = s + gmpy.mpq(x**x)

print s%(10**10)