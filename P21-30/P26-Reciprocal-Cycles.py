import re
from decimal import *

"""
Find the number d between 1 and 1000 s.t 1/d has longest recurring cycle

My approach:
        A cycle can be spotted using regex. 1/d is always of form 0.\d+
        If it has a recurring cycle, 0.\d+?(\d+?)\1\d+
        I need to calculate the division to at least as many digits as 2 * d (as my regex checks for at least 2 repetitions using look ahead)
        Python's decimal module gives arbitrary precision division

Efficient approach:
        After solving the problem, I read discussions in the forum about rep-units
        Full reptends are primes such that 1/p has cycle of p-1 digits. Given my answer, it should have occurred to me earlier :P
        7, 17, 19, 23 are all Full Reptend primes and can be found using Fermat's Little Theorem
        Link : http://mathworld.wolfram.com/FullReptendPrime.html
"""

pat = re.compile(r'0.\d+?(\d+?)\1\1\1\d+')

def largest_cycle(n, p):
    getcontext().prec = p
    a = Decimal(1)/Decimal(n)
    global pat
    m = pat.match(str(a))
    if m is None:
        return 0
    return len(m.groups()[0])

def find(p):
    l = 1
    n = 2
    for x in range(3, 1001):
        k = largest_cycle(x, p)
        if k > l:
            l = k
            n = x
    return n,l

print(find(10000))
