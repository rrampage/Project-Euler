#Project Euler - Problem 9
#Language: Python2
#Time of Completion: 18-08-2012 05:27 IST

#---IMPORT SPACE ----#
import sys

def pythTripletFinder(sum1):
    """Returns the first Pythagorean triplet for a given sum a+b+c"""
    a = 0
    b = 0
    sum1 = int(sum1)
    for x in range(1,sum1):
	for y in range(1,sum1):
	    if (x*x + y*y) == (sum1 - x -y)**2 :
		return x,y,sum1-x-y
    return 0,0,0

a= pythTripletFinder(sys.argv[1])
print a
print a[0]*a[1]*a[2] 