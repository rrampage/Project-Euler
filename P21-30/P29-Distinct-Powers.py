def ps(n):
    s = {a**b for a in range(2, n+1) for b in range(2, n+1)}
    return len(s)

print(ps(100))
