import re
from decimal import *

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
