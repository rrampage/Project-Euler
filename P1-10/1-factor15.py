#Project Euler - Problem 1
#Language: Python
#Time of Completion: 17-08-2012 14:15 IST

import sys

def factor15(n):
    #Finds the sum of all multiples of 3 and 5 lesser than n
    sum = 0
    for x in range(n):
        if x%15 == 0:
            sum = sum + x
        elif x%3 == 0:
            sum = sum + x
        elif x%5 == 0:
            sum = sum + x
    return sum

sys.argv.pop(0)
list1 = [int(x) for x in sys.argv]
for x in range(len(list1)):
	print(factor15(list1[x]))