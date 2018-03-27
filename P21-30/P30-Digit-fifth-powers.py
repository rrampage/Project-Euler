def ds(n):
    s = 0
    while (n > 0):
        s += (n%10)**5
        n //= 10
    return s

n = 0
ss = 0

for x in range(2, 1000000):
    if ds(x) == x:
        n += 1
        ss += x
print(n)
print(ss)
