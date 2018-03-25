# Problem 92
# Square Digit Chains

O = {1}
E = {89}
AO = {1}
AE = {89}

def dss(n):
    "Calculate square digit sum of a number"
    s = 0
    while n > 0:
        s += (n%10)**2
        n //= 10
    return s


def dssc(n):
    "Add all intermediate square digit sums to either O or E and the number itself to AO or AE"
    global O, E, AO, AE    
    a = dss(n)
    t = [1, 89]
    l = {a}
    while a not in O and a not in E:
        l.add(a)
        a = dss(a)
    if a in O:
        O = O.union(l)
        AO.add(n)
    else:
        E = E.union(l)
        AE.add(n)
    return

for x in range(1, 10000000):
    dssc(x)

print(len(AE))

