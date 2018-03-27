import math

f = open('p099_base_exp.txt', 'r')
l = f.readlines()
a = [list(map(int, k.strip().split(','))) for k in l]
m = -1
i = 0

for x in range(len(a)):
    c,d = a[x]
    e = d * math.log2(c)
    if e > m:
        m = e
        i = x+1
print(i)
print(m)
f.close()

