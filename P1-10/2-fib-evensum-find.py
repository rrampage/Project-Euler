#Project Euler - Problem 2
#Language: Python
#Time of Completion: 17-08-2012 14:55 IST

import sys
def fibofind(n):
    fib = []
    a = 1
    b = 1
    while a < n :
        fib.append(a)
        a,b = b,a+b
    return fib

a = fibofind(int(sys.argv[1]))
b = [x for x in a if (x%2==0)]
print(sum(b))